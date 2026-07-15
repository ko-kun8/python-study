import numbers
import pandas as pd
import re

#汚いデータを作る
data = {
    "商品名": [" りんご ", "ばなな\n", "みかん ", " ぶどう"],
    "価格": ["￥1,000", "2,500", "￥800", "￥1,200円"],
    "在庫": ["10個", "在庫なし", "5個", "20個"]
}
df = pd.DataFrame(data)
print(df)

#前後の空白を削除
df["商品名"] = df["商品名"].str.strip()
print(df)

#価格から数字だけを取り出す
def clean_price(price):
    numbers = re.findall(r"\d+", price.replace(",", ""))
    return int("".join(numbers)) if numbers else 0

df["価格"] = df["価格"].apply(clean_price)
print(df)

# 在庫を数字に変換（「在庫なし」は0にする）
def clean_stock(stock):
    if "なし" in stock:
        return 0
    numbers = re.findall(r"\d+", stock)
    return int(numbers[0]) if numbers else 0

df["在庫"] = df["在庫"].apply(clean_stock)
print(df)

#重複を削除
df = df.drop_duplicates()
print(df)