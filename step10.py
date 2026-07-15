import pandas as pd

df=pd.read_csv("data.csv", encoding="utf-8")

average_age=df["年齢"].mean()
print("年齢の平均:", average_age)

df_filtered=df[df["年齢"] >=25]
print(df_filtered)

df_filtered.to_csv("result.csv",encoding="utf-8", index=False)
print("result.csvに保存しました!")
