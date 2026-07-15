import pandas as pd

#データを作る
data = {
    "名前": ["太郎", "花子","太郎","花子","次郎"],
    "月": ["１月", "１月", "２月", "２月", "１月"] ,
    "売上": [100, 150, 200, 120, 80] ,
}

df = pd.DataFrame(data)
print(df)

#ピポットテーブルを作る
pivot = pd.pivot_table(
    df,
    values="売上",
    index="名前",
    columns="月",
    aggfunc="sum"
)
print(pivot)

#合計も表示する
pivot["合計"] = pivot.sum(axis=1)
print(pivot)

#csvに保存
pivot.to_csv("pivot.csv", encoding="utf-8")
print("pivot.csvに保存しました!")