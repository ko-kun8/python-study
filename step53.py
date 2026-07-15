import os

from step7 import f 

# 1. ターゲットが詰まっているフォルダの場所を指定
target_folder = "自動化テストフォルダ"

print("‐‐‐ファイル名の一括リネームを開始します　ーーー")

# 2. フォルダの中にあるファイルを１個ずつチェックする（ループ処理）
for file_name in os.listdir(target_folder):

    # 🌟【安全対策】「.txt」で終わるファイルだけを対象にする
    if file_name.endswith(".txt"):

        # 🌟【プロの安全ガード】もし、すでに「【自動化】」で始まっているなら飛ばす！
        if "【自動化】" in file_name:
            print(f"⏭️{file_name}はすでにリネーム済みなのでスキップします。")
            continue # 次のファイルの処理へ進む合図

        # 3. 「元の場所（パス）」と「新しい場所（パス）」の設計図を作る
        old_path = os.path.join(target_folder, file_name)
        new_path = os.path.join(target_folder, f"【自動化】_{file_name}")

        # 4. 【超新技】名前をガチャンと書き換える
        os.rename(old_path, new_path)
        print(f"✨変更前: {file_name} → 変更後: 【自動化】 _{file_name}")

print("すべて完了しました！")