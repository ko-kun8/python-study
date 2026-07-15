
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# タグで取得
print(soup.select("h1"))
print(soup.select_one("h1").text)

# classで取得（例：class="title"）
# print(soup.select(".title"))

# idで取得（例：id="main"）
# print(soup.select("#main"))

# 入れ子で取得（bodyの中のp）
print(soup.select("body p"))

# 全リンクのhrefを取得
links = soup.select("a")
for link in links:
    print(link.text, link["href"])