import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64)"
}

#画像保存用フォルダを作る
os.makedirs("images", exist_ok=True)

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

#画像タグを全部取得
images = soup.select("img")
print("画像の数:", len(images))

for i, img in enumerate(images):
    img_url = img["src"]
    #相対URLに変換
    full_url = "https://books.toscrape.com/" + img_url.replace("../", "")

    #画像をダウンロード
    img_data = requests.get(full_url, headers=headers).content
    filename = f"images/book_{i}.jpg"

    with open(filename, "wb") as f:
        f.write(img_data)

    print(f"{filename}を保存しました！")

print("全画像のダウンロード完了！") 