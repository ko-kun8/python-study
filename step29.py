import pdfplumber
import pandas as pd

#pdfを読み込む
with pdfplumber.open("sample.pdf") as pdf:
    #ページ数を確認
    print("ページ数:", len(pdf.pages))

    #1ページ目のテキストを取得
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)

    #テーブルを取得
    table = page.extract_table()
    if table:
        df = pd.DataFrame(table[1:], columns=table[0])
        print(df)
        df.to_excel("pdf_output.xlsx", index=False)
        print("pdf_output.xlsx に保存しました！")
    else:
        print("テーブルがみつかりませでした")