from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

#Chromeを起動する
driver = webdriver.Chrome()

#ページを開く
driver.get("https://quotes.toscrape.com/js/")

#少し待つ（JavaScriptが実行されるのを待つ）
time.sleep(2)

#明言を取得
quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

#ブラウザを閉じる
driver.quit()


