import os
import sys
from dotenv import load_dotenv  # 👈【修正】正しく load_dotenv だけをスマートに呼び出す

# 🌟魔法の1行：どこから起動されてもファイルを見失わないようにする
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# 【重要】同じフォルダにある「.env」ファイルを読み込む
load_dotenv()

print("ーーー 設定ファイル管理テストを開始します ーーー")

# os.environ.get() を使って、.envファイルに隠した鍵を安全に引っ張り出す
line_token = os.environ.get("LINE_API_KEY")
slack_url = os.environ.get("SLACK_URL")
db_pass = os.environ.get("DB_PASSWORD")

print("✅ .envファイルから秘密の情報を安全に読み込みました：")
# 鍵が空っぽ（None）じゃなければ、安全に最初の5文字だけ表示する
if line_token:
    print(f"・LINEトークン（先頭5文字）: {line_token[:5]}...")
else:
    print("・LINEトークン: 読み込み失敗（.envの文字を確認してください）")
    
print(f"・Slack URL: {slack_url}")
print(f"・データベースパスワード: {db_pass}")

print("ーーー 設定ファイルの管理テストが完了しました ーーー")