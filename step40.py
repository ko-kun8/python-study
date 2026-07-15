import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows Nt 10.0; Win64; x62)"
}

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1,4): #1～3ページ
    url = base_url.format(page)
    print(f"取得中:{url}")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")
    for book in books:
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").text
        price = price.encode("latin1").decode("utf-8")  # この行を追加
        availability = book.select_one(".availability").text.strip()
        data.append({
            "書籍名": title,
            "価格": price,
            "在庫": availability
        })

        time.sleep(1)

df = pd.DataFrame(data)
print(df)
print("取得件数:"), len(df)

#Excelに保存
df.to_excel("books.xlsx", index=False)
print("books.xlsx に保存しました!")