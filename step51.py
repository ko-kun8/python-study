import os

# 1.今、pythonがパソコンの「どのフォルダ」でお仕事しているかを確認する
current_dir = os.getcwd()
print(f"現在のお仕事場所（フォルダ）:\n{current_dir}\n")

# 2. 児童かの実験用に、新しく「お試しフォルダ」を１個作ってみる
new_folder_name = "自動化テストフォルダ"

# 🌟「もし同じ名前のフォルダがまだ無ければ、作る」というプロの安全対策
if not os.path.exists(new_folder_name):
    os.mkdir(new_folder_name)
    print(f"✨[{new_folder_name}]を新しく作成しました！")
else:
    print(f"⚠️ [{new_folder_name}] はすでに存在するので、新しく作りませんでした。")

print("-" * 50)

# 3. 今いるフォルダの中に「何があるか」の一覧をガサッと取得する
file_list = os.listdir(".") # "." は「現在のフォルダ」という意味

print("【このフォルダの中身一覧】")
for item in file_list:
    print(f" 📂{item}")
    