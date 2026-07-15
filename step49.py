import requests

#1.猫のトリビアをくれるAPIの「裏口窓口（URL）」
url = "http://catfact.ninja/fact"

print("--- API窓口へデータを申請します ーーー")

# 2.窓口へアクセス（requestsで普通にGETするだけ！）
response = requests.get(url)

# 3. 【超新技】届いたデータを「JSONｚ（辞書）形式」として丸ごと読み込む！
data = response.json()

# 4. 届いたＪＳＯＮ（中身はただのpythonの辞書）を表示してみる
print("【届いた生のJSONデータ】")
print(data)
print("-" * 50)

# 5. 辞書から特定のキー（"fact")を指定して、お宝データだけをっ引っこ抜く！
cat_fact = data["fact"]
length = data["length"]

print("【綺麗に取り出したデータ】")
print(f"🐱 猫の雑学:{cat_fact}")
print(f"📊 文字数: {length}文字")