import json
import requests
from bs4 import BeautifulSoup

# 🌟設定：前に成功したLINE公式のアクセストークンをそのまま使います！
LINE_ACCESS_TOKEN = "YOUR_LINE_ACCESS_TOKEN"
# 前に成功した、公式の「全員に一斉送信」する住所です
LINE_API_URL = " "YOUR_LINE_ACCESS_TOKEN"t"
book_url = "http://books.toscrape.com/"

print("ーーー 🏆 自動化ツール公式完成版 システム起動 ーーー")

try:
    # 1. 本のサイトからデータを丸ごとダウンロードする
    print("🌐 1. 本のサイトから最新データを収穫中...")
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 2. ページ内から本の一覧（h3タグ）をすべて見つける
    book_titles = soup.find_all("h3")
    
    # 3. LINEに送るための「メッセージの文章」の頭文字を用意する
    message_text = "🤖【Python最新自動化通知】\n最新の洋書入荷をお知らせします！\n"
    
    # 4. 発見した本のタイトルを、1冊ずつ文章にくっつけていく
    for book in book_titles:
        title_text = book.find("a").get("title")
        message_text += f"📖 {title_text}\n"
    
    # 5. 送りたいメッセージの形式を組み立てる（LINE公式のメッセージルール）
    payload = {
        "messages": [
            {
                "type": "text",
                "text": message_text
            }
        ]
    }
    
    # 6. 【重要】手紙の封筒（ヘッダー）に、公式アクセストークンをセット
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    
    # 7. データをJSON形式にラッピング
    json_data = json.dumps(payload)
    
    # 8. 【大サビ】LINEのサーバーに向かって、データをドカンと送信！
    print("🚀 2. 公式Messaging APIの住所へデータを送信中...")
    line_response = requests.post(LINE_API_URL, data=json_data, headers=headers)
    
    # 9. 結果確認（成功すると「200」という数字が返ってきます）
    if line_response.status_code == 200:
        print("✅ 3. LINEへの公式最新通知が正常に送信されました！スマホを確認してください！")
    else:
        print(f"⚠️ 送信失敗。エラーコード: {line_response.status_code}")
        print(f"詳細なエラー内容: {line_response.text}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")

print("ーーー 🏆 自動化ツール公式完成版 システム終了 ーーー")