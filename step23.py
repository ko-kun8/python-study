#基本のtry/except
from math import e
import numbers
from threading import excepthook


try:
    print(1 / 0)
except ZeroDivisionError:
    print("ゼロで割ることはできません！")

#ファイルが存在しない場合
try:
    with open("存在しないファイル.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("ファイルが見つかりません”")

#複数のエラーに対応
try:
    number = int("abc")
except ValueError:
    print("数字に変換できません：")
except Exceptime , e:
    print(" 予期しないエラー:", e)

#fanallyは必ず実行される
try:
    result = 10/2
    print("結果:", result)

except ZeroDivisionError:
    print ("エラーが発生しました！")
finally :
    print("処理が終わりました")