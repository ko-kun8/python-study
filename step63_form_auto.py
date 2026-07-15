import pandas as pd  # 🌟新顔：大量のデータや表を爆速で処理する最強の相棒

# 1. 公開したスプレッドシートのIDをここに貼り付けます
SPREADSHEET_ID = "15J8c8KhUBTGzzb1oSt4qAelj2TBx6Y39QMMebjxJxic"

# 2. Googleスプレッドシートを「CSV」というPythonが読みやすい形式でダウンロードする魔法のURL
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv"

print("ーーー Googleフォーム回答データの自動検知・読込を開始します ーーー")

try:
    # 3. 【大サビ】インターネット上のスプレッドシート（CSV）を一撃で読み込んで表にする
    # ※requestsを使わずに、pandasが裏で勝手に通信してデータを取ってきてくれます！
    df = pd.read_csv(CSV_URL)

    print("フォームの回答データをチェック...")

    # 4. 回答が1件でもあるか確認する
    if not df.empty:
        # 一番最新の回答（表の一番下の行）をピンポイントで取得する
        latest_row = df.iloc[-1]

        print("\n✨ 【新着】Googleフォームへの回答を検知しました！")
        print("-" * 40)
        print(f"⏰ タイムスタンプ : {latest_row.iloc[0]}")
        print(f"👤 お名前         : {latest_row.iloc[1]}")
        print(f"💬 内容           : {latest_row.iloc[2]}")
        print("-" * 40)
    else:
        print("まだフォームの回答は０件です。フォームからテスト回答を送信してみてください！")

except Exception as e:
    print(f"データの読み込み中にエラーが発生しました: {e}")