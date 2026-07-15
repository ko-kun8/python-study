import pandas as pd
df=pd.read_csv("data.csv", encoding="utf-8")
print(df)

print(df.isnull())

print(df.isnull().sum())

df_drop=df.dropna()
print(df_drop)

df_fill=df.fillna({"年齢":0, "都市":"不明"})
print (df_fill)