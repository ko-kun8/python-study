import pandas as pd
import glob

#フォルダ内の全csvを取得
files = glob.glob("excel_files/*.csv")
print(files)

#全ファイルを読み込んでまとめる
all_data = []
for file in files:
    df = pd.read_csv(file, encoding="utf-8")
    all_data.append(df)

#縦につなげる
df_all = pd.concat(all_data)
print(df_all)

#合計売上を計算
print("合計売上:", df_all["売上"].sum())

#まとめてcsvに保存
df_all.to_csv("all_data.csv", encoding="utf-8",index=False)
print("all_data.csvに保存しました!")