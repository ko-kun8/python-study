# 🌟魔法の1行：隣のファイルから設計図（TradingBot）をスカウトしてくる！
from bot_module import TradingBot

print("ーーー 🏆 モジュール分割システム 起動 ーーー")

# 1. 別ファイルから読み込んだ設計図を使って、ドル円ロボを誕生させる
robot_usd = TradingBot("モジュールタロウ", "USD/JPY")

# 2. ロボに仕事を命令する
robot_usd.order("買い", 5000)
robot_usd.report_profit(3500)

print("ーーー 🏆 モジュール分割システム 終了 ーーー")