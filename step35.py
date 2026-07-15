import requests
from bs4 import BeautifulSoup
import time

# 複数ページを巡回する例
base_url = "https://quotes.toscrape.com/page/{}/"

all_quotes = []

for page in range(1, 4):  # 1ページ目〜3ページ目
    url = base_url.format(page)
    print(f"取得中: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 名言を取得
    quotes = soup.select(".quote .text")
    for quote in quotes:
        all_quotes.append(quote.text)

    # サーバーに負荷をかけないよう1秒待つ
    time.sleep(1)

print("取得した名言の数:", len(all_quotes))
for q in all_quotes[:5]:  # 最初の5個だけ表示
    print(q)

    import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://example.com"
response = requests.get(url, headers=headers)
print(response.status_code)