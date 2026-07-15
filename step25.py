import argparse

#員数を受け取る設定
parser = argparse.ArgumentParser(description="売上集計ツール")
parser.add_argument("filename", help="読み込むcsvファイル名")
parser.add_argument("--output", help="出力ファイル名", default="output.csv")
parser.add_argument("--limit", help="最低売上金", type=int, default=0)

args = parser.parse_args()

print("読み込むファイル:", args.filename)
print("出力ファイル:", args.output)
print("最低売上金:", args.limit)