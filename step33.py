import requests
from bs4 import BeautifulSoup

#htmlを取得する
url = "https://example.com"
response = requests.get(url)
response.encoding = "utf-8"

#BeautifulSoupでパースする
soup = BeautifulSoup(response.text, "html.parser")

#タイトルを取得
print(soup.title)
print(soup.title.text)

#h1タグを取得
print(soup.find("h1"))
print(soup.find("h1").text)

#pタグを全部取得
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)

#リンクを全部取得
links = soup.find_all("a")
for link in links:
    print(link.text,link.get("href"))