import logging
import os
import sys

# 🌟魔法の1行：どこから起動されてもファイルを見失わないようにする
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# 【ログの設定】「app.log」というファイルに、日時の形式を指定して記録する設定
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8" # 日本語が文字化けしないようにするお守り
)

print("ーーー ログ記録テストプログラムを開始します ーーー")
logging.info("プログラムが正常に起動しました。")

try:
    # 1. 正常な動きの記録
    print("データを処理中...")
    logging.info("データの処理が順調に完了しました。")

    # 2. わざとエラーを起こしてみる（ゼロで割り算するエラー）
    print("危険な計算に挑戦します...")
    result = 10 / 0

except Exception as e:
    # エラーが起きたら、その内容をガチでログファイルに書き残す！
    print(f"エラーが発生しました。ログに記録します。")
    logging.error(f"深刻なエラーが発生しました: {e}, exc_imfo=True")

print("ーーー プログラムが終了しました。app.logを確認してください ーーー")
logging.info("プログラムが終了しました。\n")