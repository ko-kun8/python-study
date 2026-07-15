# ファイルに書き込む
with open("test.txt", "w") as f:
    f.write("こんにちは\n")
    f.write("Pythonの練習中です\n")

# ファイルを読み込む
with open("test.txt", "r") as f:
    content = f.read()
    print(content)