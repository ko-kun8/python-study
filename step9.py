import pandas as pd

df = pd.read_csv("data.csv",encoding="utf-8")

print(df)

print(df["名前"])

print(df.shape)
