from re import A
import requests 
from bs4 import BeautifulSoup # 🌟新顔：HTMLを綺麗に解析してくれるスープ屋さん

# 1. 情報をかき集めたいターゲットのURL（今回はYahoo!ニュースのトップ）
URL = "http://news.yahoo.co.jp/"

print("ーーー Webスクレイピング (yahoo!ニュース抽出) を開始します ーーー")

try:
    # 2. 【通信】Yahoo!ニュースのホームページの「設計図（HTML）」を丸ごと取ってくる
    response = requests.get(URL)

    # 3. 【解析】取ってきた設計図を、BeautifulSoupに渡して解析できるようにする
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. 【最新修正】ニュースのリンク（aタグ）を広めにかき集める
    # クラス名が頻繁に変わるため、トップページの主要ニュース枠のリンクをまとめて取得します
    articles = soup.select("a.v99-CoreNaviListItem, a.sc-fEldeZ, a[href*='news.yahoo.co.jp/pickup']")
    
    print(f"無事にデータを取得しました。現在の最新ニュースをお届けします！\n")
    print("=" * 50)

    # 5. 【出力】見つかったニュースを上から順番に番号をつけて画面に表示する
    for i, article in enumerate(articles, 1):
        title = article.text # タグの中から「文字（ニュースのタイトル）」だけを抜き出す
        print(f"{i}位 : {title}")

    print("=" * 50)

except Exception as e:
    print(f"スクレイピング中にエラーが発生しました: {e}")
    