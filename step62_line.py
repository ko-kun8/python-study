import requests  # 🌟ネット越しの通信でお馴染みの相棒

# 1. LINEから発行してもらう「あなた専用の魔法のトークン（鍵）」
# ※後ほど、本物の鍵に書き換えます！
LINE_TOKEN = "YOUR_LINE_NOTIFY_TOKEN"

# LINE Notifyの送り先住所（これは全員共通のURLです）
LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"

print("ーーー LINEへの通知処理を開始します ーーー")

try:
    # 2. LINEに送るデータを組み立てる（「message」という名前の箱に入れるルールです）
    payload = {
        "message": "\n🤖【Python自動化通知】\nLINEへの通知テストも大成功です！🚀"
    }
    
    # 3. 【超重要】「この鍵を使うよ」という証明書をセットする
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}"
    }
    
    # 4. 【大サビ】LINEのサーバーに向かって、データをドカンと送信！
    response = requests.post(LINE_NOTIFY_URL, data=payload, headers=headers)
    
    # 5. 送信結果のチェック（LINEは成功すると200という数字を返してくれます）
    if response.status_code == 200:
        print("✨ LINEへの通知が正常に送信されました！スマホを確認してください。")
    else:
        print(f"⚠️ 送信に失敗しました。LINEからの返答コード: {response.status_code}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")