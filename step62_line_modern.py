import json
import requests
import os  # 👈【追加】1. フォルダの場所を操作する「os」という相棒を召喚
import sys  # 👈【追加】2. システムの情報を司る「sys」という相棒を召喚

# 🌟設定：あなたのLINEの2つの鍵をここに貼り付けます
LINE_CHANNEL_SECRET =  "YOUR_LINE_ACCESS_TOKEN"
LINE_ACCESS_TOKEN = "YOUR_LINE_ACCESS_TOKEN"
# Messaging APIで「全員に一斉送信（ブロードキャスト）」する公式の住所です
LINE_API_URL = "https://api.line.me/v2/bot/message/broadcast"

# 👈【追加】3. 「このファイル自身が置いてあるフォルダ」を強制的に作業場所に指定する魔法
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print("ーーー 最新LINE Messaging APIでの通知処理を開始します ーーー")

try:
    # 1. 送りたいメッセージの形式を組み立てる（LINE公式のルールです）
    payload = {
        "messages": [
            {
                "type": "text",
                "text": "🤖【Python最新自動化通知】\nLINE Messaging APIでの通知連携に成功しました！\n次世代の自動化システム、爆誕です。🚀"
            }
        ]
    }
    
    # 2. 【超重要】手紙の封筒（ヘッダー）に、アクセストークンなどの証明書をセット
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    
    # 3. データをJSON形式にラッピング
    json_data = json.dumps(payload)
    
    # 4. 【大サビ】LINEのサーバーに向かって、データをドカンと送信！
    response = requests.post(LINE_API_URL, data=json_data, headers=headers)
    
    # 5. 結果確認（LINE Messaging APIは成功すると「200」という数字が返ってきます）
    if response.status_code == 200:
        print("✨ LINEへの最新通知が正常に送信されました！スマホのLINEアプリを確認してください。")
    else:
        print(f"⚠️ 送信失敗。エラーコード: {response.status_code}")
        print(f"詳細なエラー内容: {response.text}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")