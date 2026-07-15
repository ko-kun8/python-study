import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

base_url = "https://quotes.toscrape.com/page/{}/"

data = []

for page in range(1, 4):
    url = base_url.format(page)
    print(f"取得中: {url}")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")
    for quote in quotes:
        text = quote.select_one(".text").text
        author = quote.select_one(".author").text
        data.append({"名言": text, "作者": author})

    time.sleep(1)

# DataFrameに変換
df = pd.DataFrame(data)
print(df)

# CSVに保存
df.to_csv("quotes.csv", encoding="utf-8", index=False)
print("quotes.csv に保存しました！")
# --- ここから書き換え ---

# 1. Excel専用の文字ルール「utf_8_sig」にしてCSV保存（文字化け対策）
df.to_csv("quotes.csv", encoding="utf-8-sig", index=False)

# 2. 【超重要】Excelファイル（.xlsx）としても保存して、最初から幅を広げる！
with pd.ExcelWriter("quotes.xlsx", engine="openpyxl") as writer:
    df.to_csv("quotes.csv", encoding="utf-8-sig", index=False) # CSVも一応残す
    df.to_excel(writer, sheet_name="名言リスト", index=False)
    
    # openpyxlの技を使って、A列とB列の幅を自動でガッツリ広げる
    ws = writer.sheets["名言リスト"]
    ws.column_dimensions["A"].width = 70  # 名言は長いので幅70
    ws.column_dimensions["B"].width = 25  # 作者は幅25

print("文字化けなし＆幅広の『quotes.xlsx』と『quotes.csv』を保存しました！")