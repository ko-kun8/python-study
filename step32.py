import requests

#htmlを取得する
url = "https://example.com"
response = requests.get(url)

#ステータスコードを認識
print("ステータスコード:", response.status_code)

#htmlの中身を表示
print(response.text[:500]) #最初の500文字だけ表示

#エンコーディングを設定
response.encoding = "utf-8"
print("エンコーディング:", response.encoding)