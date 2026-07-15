import os
import sys
import requests

# 🌟魔法の1行：フォルダの場所を絶対に固定する
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print("ーーー 🕵️‍♂️ ネットワーク徹底検査を開始します ーーー")

try:
    # 1. 検査その①：世界で一番安定しているGoogleに繋がるか？
    print("🔍 検査1: Google（世界標準のサイト）に繋がるかテスト中...")
    google_res = requests.get("https://www.google.com", timeout=5)
    print(f" 🟢 Googleへの接続に成功しました！（ステータス: {google_res.status_code}）")
    
    # 2. 検査その②：問題のLINEの窓口に繋がるか？
    print("\n🔍 検査2: LINE Notifyのサーバーに繋がるかテスト中...")
    line_res = requests.get("https://notify-api.line.me/", timeout=5)
    print(f" 🟢 LINEへの接続に成功しました！（ステータス: {line_res.status_code}）")

except Exception as e:
    print(f"\n❌ 検査中にエラーが発生しました: {e}")

print("\nーーー 🕵️‍♂️ ネットワーク徹底検査を終了します ーーー")