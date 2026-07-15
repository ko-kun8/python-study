# 🌟ロボの設計図（クラス）だけを専門に保管するファイル（モジュール）

class TradingBot:
    def __init__(self, bot_name, currency_pair):
        self.name = bot_name
        self.pair = currency_pair
        self.total_profit = 0
        print(f"🤖 [モジュール] ロボ『{self.name}』が正常に読み込まれました。（担当: {self.pair}）")

    def order(self, direction, amount):
        print(f"🚀 【{self.name}】{self.pair} を {amount} 通貨、[{direction}] で注文！")

    def report_profit(self, win_money):
        self.total_profit += win_money
        print(f"💰 【{self.name}】現在のトータル利益: ＋{self.total_profit}円")