import pandas as pd

df1 = pd.read_csv("data.csv", encoding="utf-8")
df2 = pd.read_csv("data2.csv", encoding="utf-8")

print(df1)
print(df2)

df_merge = pd.merge(df1, df2, on="名前")
print(df_merge)

df_merge_all = pd.merge(df1, df2, on="名前", how="outer")
print(df_merge_all)

df_concat = pd.concat([df1, df2])
print(df_concat)