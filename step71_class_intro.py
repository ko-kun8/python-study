print("ーーー 🤖 クラス入門：自動売買ロボシステム起動 ーーー")

# 1. 自動売買ロボの「設計図（クラス）」を定義する
class TradingBot:
    # 2. ロボが誕生した瞬間に、自動で名前と取引ペアを記憶する（初期化）
    def __init__(self, bot_name, currency_pair):
        self.name = bot_name              # ロボの名前を記憶
        self.pair = currency_pair          # 取引する資産（ドル円やゴールド）を記憶
        self.total_profit = 0              # 最初、利益は0円
        print(f"🤖 ロボ『{self.name}』が誕生しました！（担当: {self.pair}）")

    # 3. ロボの「動き（関数）」を定義する：注文を出す
    def order(self, direction, amount):
        print(f"🚀 【{self.name}】{self.pair} を {amount} 通貨、[{direction}] で注文しました！")

    # 4. ロボの「動き（関数）」を定義する：利益を報告する
    def report_profit(self, win_money):
        self.total_profit += win_money    # 利益を箱に足し算する
        print(f"💰 【{self.name}】現在までのトータル利益: ＋{self.total_profit}円")


# 🌟 ここから本番：設計図から「本物のロボ」を誕生させる！

# 5. ドル円担当のロボ「タロウ」を誕生させる（実体化）
robot_usd = TradingBot("ドル円タロウ", "USD/JPY")

# 6. ゴールド担当のロボ「ゴールドエッジ」を誕生させる（実体化）
robot_gold = TradingBot("ゴールドエッジ", "Gold")

print("\n--- 🤖 ロボたちに仕事を命令します ---")

# 7. ドル円タロウに「買い注文」を出させる
robot_usd.order("買い", 10000)
robot_usd.report_profit(5000)  # 5000円儲かった！

# 8. ゴールドエッジに「売り注文」を出させる
robot_gold.order("売り", 2000)
robot_gold.report_profit(12000) # 12000円儲かった！

print("ーーー 🤖 クラス入門 システム終了 ーーー")