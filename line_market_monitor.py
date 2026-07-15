# -*- coding: utf-8 -*-
"""
ドル円・ゴールド等を監視し、一定以上の変動で LINE に通知するスクリプト。

必要なライブラリ: pip install -r requirements_market_monitor.txt
"""

from __future__ import annotations

import textwrap
import time
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Any

import requests
import yfinance as yf

# ---------------------------------------------------------------------------
# ▼▼▼ ここだけ書き換えれば動きます（LINE） ▼▼▼
# ---------------------------------------------------------------------------
# LINE Developers で「Messaging API」のチャネルを作成し、
# 「チャネルアクセストークン（長期）」をコピーして貼り付けてください。
# あなたの LINE アカウントでその「友だち追加」QR を読み取っておくと、
# ブロードキャストで自分の LINE に届きます（ユーザーIDの設定は不要）。
LINE_CHANNEL_ACCESS_TOKEN = "ここにチャネルアクセストークンを貼り付け"

# 価格チェックの間隔（秒）。5分 = 300
CHECK_INTERVAL_SECONDS = 10
# ---------------------------------------------------------------------------

LINE_BROADCAST_URL = "https://api.line.me/v2/bot/message/broadcast"
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q={q}&hl=en&gl=US&ceid=US:en"


def build_watchlist() -> list[dict[str, Any]]:
    """
    監視する銘柄のリスト。threshold は「前回価格からの絶対変動」がこの値以上で通知。
    news_queries は Google ニュース RSS の検索語（急変時にタイトルを拾う）。
    例: ユーロドルを足す場合は下のコメントを参考に 1 行追加してください。
    """
    return [
        {
            "symbol": "GC=F",
            "label": "ドル円 (USD/JPY)",
            "threshold": 0.01,  # 円建て 0.1 以上
            "news_queries": ["USDJPY", "USD JPY forex"],
        },
        {
            "symbol": "XAUUSD=X",
            "label": "ゴールド (XAU/USD)",
            "threshold": 2.0,  # ドル建て 2 以上
            "news_queries": ["Gold market", "XAUUSD gold price"],
        },
        # 追加例（コメントを外して使う）:
        # {
        #     "symbol": "EURUSD=X",
        #     "label": "ユーロドル (EUR/USD)",
        #     "threshold": 0.0010,
        #     "news_queries": ["EURUSD", "Euro dollar forex"],
        # },
    ]


def fetch_last_close(symbol: str) -> float | None:
    """yfinance で直近の終値（できるだけ新しいバー）を取得。"""
    try:
        t = yf.Ticker(symbol)
        # 直近数日の 5 分足の最終行 ≒ 直近価格
        hist = t.history(period="5d", interval="5m", auto_adjust=False)
        if hist is None or hist.empty:
            return None
        return float(hist["Close"].iloc[-1])
    except Exception:
        return None


def _strip_ns(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def parse_rss_titles(xml_bytes: bytes, limit: int) -> list[str]:
    root = ET.fromstring(xml_bytes)
    titles: list[str] = []

    for el in root.iter():
        if _strip_ns(el.tag) != "item":
            continue
        title_el = None
        for child in el:
            if _strip_ns(child.tag) == "title":
                title_el = child
                break
        if title_el is None or not title_el.text:
            continue
        t = title_el.text.strip()
        if t and t not in titles:
            titles.append(t)
        if len(titles) >= limit:
            break
    return titles


def fetch_google_news_titles(queries: list[str], max_titles: int = 3) -> list[str]:
    """Google ニュース RSS から記事タイトルを最大 max_titles 件まで。"""
    collected: list[str] = []
    per_query = max(1, max_titles // max(1, len(queries)))

    for q in queries:
        if len(collected) >= max_titles:
            break
        url = GOOGLE_NEWS_RSS.format(q=urllib.parse.quote(q))
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            batch = parse_rss_titles(r.content, per_query + 2)
            for t in batch:
                if t not in collected:
                    collected.append(t)
                if len(collected) >= max_titles:
                    break
        except Exception:
            continue
    return collected[:max_titles]


def send_line_broadcast(text: str) -> bool:
    if not LINE_CHANNEL_ACCESS_TOKEN or LINE_CHANNEL_ACCESS_TOKEN.startswith("ここに"):
        print("エラー: ファイル上部の LINE_CHANNEL_ACCESS_TOKEN を設定してください。")
        return False
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    body = {"messages": [{"type": "text", "text": text}]}
    try:
        r = requests.post(LINE_BROADCAST_URL, headers=headers, json=body, timeout=15)
        if r.status_code != 200:
            print(f"LINE API エラー: {r.status_code} {r.text}")
            return False
        return True
    except Exception as e:
        print(f"LINE 送信失敗: {e}")
        return False


def format_alert(
    label: str,
    symbol: str,
    prev: float,
    cur: float,
    headlines: list[str],
) -> str:
    delta = cur - prev
    sign = "+" if delta >= 0 else ""
    lines = [
        f"【相場アラート】{label}",
        f"シンボル: {symbol}",
        f"前回: {prev:.5f} → 現在: {cur:.5f} ({sign}{delta:.5f})",
        "",
        "▼ 関連ニュース（Google News）",
    ]
    if headlines:
        for i, h in enumerate(headlines, 1):
            lines.append(f"{i}. {h}")
    else:
        lines.append("（取得できませんでした）")
    return "\n".join(lines)


def main() -> None:
    watchlist = build_watchlist()
    last_prices: dict[str, float | None] = {w["symbol"]: None for w in watchlist}

    print("監視を開始しました（初回は基準価格のみ記録し、通知はしません）。")
    print(f"銘柄数: {len(watchlist)} / 間隔: {CHECK_INTERVAL_SECONDS} 秒")

    while True:
        for w in watchlist:
            sym = w["symbol"]
            label = w["label"]
            threshold = float(w["threshold"])
            news_queries = list(w["news_queries"])

            price = fetch_last_close(sym)
            if price is None:
                print(f"[{sym}] 価格取得失敗。スキップ。")
                continue

            prev = last_prices.get(sym)
            last_prices[sym] = price

            if prev is None:
                print(f"[{sym}] 基準価格を記録: {price:.5f}")
                continue

            if abs(price - prev) >= threshold:
                headlines = fetch_google_news_titles(news_queries, max_titles=3)
                msg = format_alert(label, sym, prev, price, headlines)
                # LINE は長文制限があるため折り返し
                msg = textwrap.shorten(msg, width=4500, placeholder="…")
                print(f"[{sym}] 変動検知。LINE 送信中…")
                send_line_broadcast(msg)
            else:
                print(f"[{sym}] 変動小: {prev:.5f} → {price:.5f}")

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
