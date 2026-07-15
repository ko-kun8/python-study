from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# ページを開く
driver.get("https:\\quotes.toscrape.com/login")
time.sleep(1)

#テキストを入力する
driver.find_element(By.NAME, "username").send_keys("test")
driver.find_element(By.NAME, "password").send_keys("test")

#ボタンをクリックする
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep

#ログイン後のページタイトルを確認
print("タイトル:", driver.title)
print("URL:",driver.current_url)

#スクロールする
driver.execute_script("window.scrollTo(0,500)")
time.sleep(1)

#明言を取得
quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes[:3]:
    print(quote.text)

driver. quit()