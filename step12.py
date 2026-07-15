import pandas as pd

df=pd.read_csv("data.csv", encoding="utf-8")
print(df)

df_25=df[df["年齢"] >=25]
print(df_25)

df_tokyo=df[df["都市"]=="東京"]
print(df_tokyo)

df_multi=df[(df["年齢"] >= 22) & (df["都市"] !="東京")]
print(df_multi)
