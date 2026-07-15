import requests

#通常のリクエスト（毎回ヘッダーを書く）
headers = {
    "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64)"
}

url = "https://quotes.toscrape.com/page/1/"
response = requests.get(url,headers=headers)
print("通常リクエスト:",response.status_code)

#セッションを使う（ヘッダーを１回設定すれば使い回せる
session = requests.Session()
session.headers.update(headers)

response1 = session.get("https://quotes.toscrape.com/page/1/")
print("セッション１ページ目:",response1.status_code)

resoinse2 = session.get("https://quotes.toscrape.com/page/1/")
print("セッション２ページ目:",resoinse2.status_code)

#クッキーを確認
print("クッキー:",session.cookies)
