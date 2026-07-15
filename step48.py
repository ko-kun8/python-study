# 🌟同期処理（1行ずつ順番に実行するモード）のPlaywrightを呼び出す
from playwright.sync_api import sync_playwright

# 1. Playwrightのロボットを起動
with sync_playwright() as p:
    
    # 2. 本物のブラウザ（Chromium）を起動。
    # headless=False にすると、Seleniumの時のように本物の画面がポコンと目の前に現れます。
    browser = p.chromium.launch(headless=True)
    
    # 3. 新しいタブ（ページ）を開く
    page = browser.new_page() 

    # 4. サイトへ突撃
    page.goto("https://quotes.toscrape.com/")
    
    # 5. 【超重要】名言（class="text"）を全員分キャッチする
    # locator（ロケーター）という、ピンポイントで場所を指し示す最新の技を使います。
    quotes = page.locator(".text")
    
    print("ーーー Playwrightが爆速でデータを回収中 （ヘッドレス）ーーー")
    
    # 6. 最初から3個だけ取り出して画面に表示
    for i in range(3):
        # .nth(i) で「i番目のデータ」を指定し、.text_content() で文字を抜きます
        quote_text = quotes.nth(i).text_content()
        print(f"{i+1}個目の名言: {quote_text}")
        
    # 7. ブラウザを安全に閉じる
    browser.close()

print("すべて完了しました！")