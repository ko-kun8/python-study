import pandas as pd
df=pd.read_csv("data.csv", encoding="utf-8")

print(df["年齢"].sum())

print(df["年齢"].mean())

print(df["年齢"].max())

print(df["年齢"].min())

print(df["年齢"].count())
df2=pd.read_csv("data.csv", encoding="utf-8")
df2["人数"]=1
print(df2.groupby("都市")["人数"].sum())
