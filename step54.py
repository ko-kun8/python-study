import os 
import shutil

# 1. 整理したい対象のフォルダ
target_folder = "自動化テストフォルダ"

print("‐‐‐ファイルの自動整理を開始しますーーー")

# 2. フォルダの中にあるファイルを１個ずつチェックする
for file_name in os.listdir(target_folder):

    # 住所（パス）を合体して作成
    file_path = os.path.join(target_folder, file_name)
    
    # 【安全対策】フォルダではなく「ファイル」の場合だけ処理する
    if os.path.isfile(file_path):

        # 3. ファイルの拡張子（.txt や.xlsx)をチェックして、行先を決める
        if file_name.endswith(".txt"):
            sub_folder_name = "テキストファイル"
        elif file_name.endswith(".xlsx") or file_name.endswith(".csv"):
            sub_folder_name ="エクセル・csvファイル"
        else:
            sub_folder_name = "その他"

        # 4. 行先となるフォルダのフル住所を作る
        destination_folder = os.path.join(target_folder, sub_folder_name)

        # 5. もしその仕分け用フォルダがまだなければ、自動で作る
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
            print(f"新しいフォルダ「{sub_folder_name}」を作成しました。")

        # 6. ファイルを仕分け用フォルダの中に移動（お引越し）させる
        shutil.move(file_path, destination_folder)
        print(f"フォルダ「{sub_folder_name}」へ移動: {file_name}")

print("全ての整理が完了しました！")
