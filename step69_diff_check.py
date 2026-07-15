import os
import sys

# 🌟魔法の1行：どこから起動されてもファイルを見失わないようにする
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print("ーーー データの差分チェックテストを開始します ーーー")

# 1. 【前回のデータ】（昨日までに確認していた案件のIDリストなど）
yesterday_data = ["JOB-001", "JOB-002", "JOB-003"]

# 2. 【最新のデータ】（今スクレイピングして取得してきた最新のリスト）
# ※「JOB-004」と「JOB-005」が新しく追加されています！
today_data = ["JOB-002", "JOB-003", "JOB-004", "JOB-005"]

try:
    # 3. 【大サビ】リストを「set（集合）」に変換して、引き算を行う！
    yesterday_set = set(yesterday_data)
    today_set = set(today_data)
    
    # 最新データ（今日）から、古いデータ（昨日）をガツンと引き算する！
    new_items = today_set - yesterday_set
    
    # 4. 結果を画面にわかりやすく表示する
    print(f"📊 昨日のデータ数: {len(yesterday_set)}件")
    print(f"📊 今日のデータ数: {len(today_set)}件")
    
    if new_items:
        print(f"🔥 【新着発見！】新しく追加されたデータは以下の {len(new_items)} 件です：")
        # setのままだと扱いづらいので、リストに戻してループで回す
        for item in list(new_items):
            print(f" 🆕 {item}")
    else:
        print("✨ 新着データはありませんでした（前回と同じです）。")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")

print("ーーー データの差分チェックテストが完了しました ーーー")