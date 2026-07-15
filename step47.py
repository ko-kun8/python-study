import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime  # ✨新アイテム：現在の時刻を扱う道具

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://quotes.toscrape.com/page/1/"

print("ーーー 24時間自動パトロールロボット、起動します！ ーーー")

# 🌟新技：無限ループ（プログラムをあえて終了させずに、ずっと動かし続ける）
while True:
    try:
        # 1. 現在の時刻を「何時何分何秒」の形でキレイに取得する
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 2. サイトにアクセスしてデータを取得
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 3. 1番目の名言だけをピンセットで抜く
        first_quote = soup.select_one(".text").text
        
        # 4. 何時に、どんなデータが取れたかを画面に報告する
        print(f"【{now}】 パトロール成功！")
        print(f"現在の1番目の名言: {first_quote[:30]}...")
        print("-" * 40)
        
    except Exception as e:
        # もしネットが切れるなどのエラーが起きても、ロボットを止めずにエラーを表示する
        print(f"【警告】エラーが発生しました: {e}")
    
    # 🌟ここが超重要！次のパトロールまで「5秒間」気絶（待機）する
    # 実務ではここを「3600（1時間）」や「86400（1日）」にします
    time.sleep(5)