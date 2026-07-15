import os 
import openpyxl
import requests
import json

# 🌟設定：あなたのSlack Webhook URLをここに貼り付けてください
SLACK_WEBHOOK_URL = "YOUR_SLACK_WEBHOOK_URL"

target_folder = "自動化テストフォルダ"
excel_name = "【最新】本日の集計データ.xlsx"
excel_path = os.path.join(target_folder, excel_name)

print("ーーー総合自動化システム ( Excel作製 → Slack通知）を開始しますーーー")

try:
    # === 🛠️ 第1ステージ: Excelファイルの自動作成 ===
    print("[1\2] Excelファイルを生成中...")

    wb  = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "売上集計"

    # テストデータを流し込む
    sheet["A1"] = "日付"
    sheet["B1"] = "商品名"
    sheet["C1"] = "金額"
    
    sheet["A2"] = "2026-07-02"
    sheet["B2"] = "Python自動化スクリプト"
    sheet["C2"] = "30000"

    wb.save(excel_path)
    print(f"Excelファイルの作成に成功しました！ ➔ {excel_path}　")

    # === 🔔 第2ステージ: Slackへの完了通知 ===
    print("⏳ [2/2] Slackへ処理結果を通知中...")
    
    # Slackに送るメッセージを組み立てる（ファイル名などを変数にして再利用！）
    notice_message = (
        f"🤖【システム自動通知】\n"
        f"データの集計処理が正常に完了しました！\n\n"
        f"📄 作成ファイル: {excel_name}\n"
        f"📂 保存先: {target_folder}\n"
        f"✨ 今日の自動化タスクはすべて大成功です！"
    )
    
    message_data = {"text": notice_message}
    json_data = json.dumps(message_data)
    
    # Slackに送信
    response = requests.post(SLACK_WEBHOOK_URL, data=json_data)
    
    if response.text == "ok":
        print("✨ Slackへの通知も100%成功しました！")
    else:
        print(f"⚠️ Slack通知でエラーが返ってきました: {response.text}")

    print("🏁 ーーー すべての連続自動化処理が正常終了しました ーーー")

except Exception as e:
    print(f"❌ システムの途中でエラーが発生しました: {e}")