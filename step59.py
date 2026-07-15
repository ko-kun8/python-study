import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. Googleに「私は怪しい者ではありません」と証明する鍵ファイル（後ほど用意します）
JSON_KEY_FILE = "credentials.json"

print("ーーー Googleスプレッドシートの操作を開始します ーーー")

try:
    # 2. 【新技】Googleにアクセスするための権限セットを作る
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scope)
    
    # 3. Googleにログインする（承認）
    client = gspread.authorize(creds)
    
    # 4. 【超重要】操作したいスプレッドシートを「名前」で指定して開く
    # （※事前にGoogleドライブ上に作っておく必要があります）
    spreadsheet = client.open("Python自動化テスト")
    
    # 5. 「一番最初のシート（シート1）」を選択
    sheet = spreadsheet.get_worksheet(0)
    
    # 6. 【読み込み】A1マスのデータを読み込んで画面に出してみる
    a1_value = sheet.acell("A1").value
    print(f"📖 現在のA1マスの値: {a1_value}")
    
    # 7. 【大サビ・書き込み】A2マスにPythonから文字を書き込んでみる！
    sheet.update_acell("A2", "Pythonからこんにちは！")
    print("✍️ A2マスに文字を書き込みました！")
    
    print("✨ すべての処理が正常に完了しました！")

except Exception as e:
    print(f"❌ エラーが発生しました（鍵がまだ無いためです）: {e}")
