import pandas as pd

df=pd.read_csv("data.csv", encoding="utf-8")
print(df)

df["年代"]=df["年齢"]//10*10
print(df)

df=df.rename(columns={"名前": "氏名", "都市": "居住地"})
print(df)

df=df.drop(columns=["年代"])
print(df)

df["氏名"]=df["氏名"].apply(lambda x: x + "さん")
print(df)
