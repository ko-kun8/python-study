import shutil
import os
# 1. コピー元のファイル名と、コピー先の場所（フォルダ）を決める
source_file = "test.txt"
target_folder = "自動化テストフォルダ"

# 🌟【安全対策】もしコピー元のファイルが本当に存在するかチェック
if os.path.exists(source_file):

    # 2. 【超新技】ファイルをフォルダの中にコピーする！
    shutil.copy(source_file, target_folder)
    print(f"✨[{source_file}]を[{target_folder}]の中にコピーしました！")

    # 3. 【応用】移動（切り取り）させたい場合はこう書きます（今回はコメントアウト）
    # shutil.move(source_file, target_folder)

else:
    print(f"⚠️コピー元の「{source_file}」が見つかりませんでした。")
    print("※もしよければ、代わりに「step51.py」などをコピー元に指定してみてください！")