import json
import requests  # 🌟新顔：インターネット越しにデータを送る大ボス

# 1. Slackから発行してもらう「あなた専用の魔法のURL」
# ※後ほど、本物のURLに書き換えます！
SLACK_WEBHOOK_URL = "YOUR_SLACK_WEBHOOK_URL"

# 2. Slackのチャット画面に送りたいメッセージの内容を決める
message_data = {
    "text": "🤖【Python自動化通知】\nExcelファイルの自動生成が完了しました！\n本日も作業お疲れ様でした。✨"
}

print("ーーー Slackへの通知処理を開始します ーーー")

try:
    # 3. 【超重要】メッセージデータをSlackが読める形式（JSON）に変換する
    json_data = json.dumps(message_data)
    
    # 4. 【大サビ】魔法のURLに向かって、インターネット越しにデータをドカンと送信！
    response = requests.post(SLACK_WEBHOOK_URL, data=json_data)
    
    # 5. Slack側から「無事に受け取ったよ（ok）」と言われたかチェック
    if response.text == "ok":
        print("✨ Slackへの通知が正常に送信されました！チャット画面を確認してください。")
    else:
        print(f"⚠️ 送信は試みましたが、Slackからの返答が違います: {response.text}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")