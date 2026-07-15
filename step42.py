from selenium import webdriver
from selenium .webdriver.common.by import  By
import time
driver = webdriver.Chrome()

#ログインページを開く
driver.get("https://quotes.toscrape.com/login")
time.sleep(1)

#ログイン情報を入力
driver.find_element(By.NAME, "username").send_keys("test")
driver.find_element(By.NAME, "password").send_keys("test")
driver.find_element(By.CSS_SELECTOR, f"input[type='submit']").click()
time.sleep(2)

#ログイン後のページから名言を全部取得
print("ログイン後のURL:", driver.current_url)

#複数ページを巡回
all_quotes = []

for page in range(1, 4):
    driver.get(f"https://quotes.toscrape.com/page/{page}/")
    time.sleep(1)

    quotes = driver.find_elements(By.CLASS_NAME, "text")
    authors = driver.find_elements(By.CLASS_NAME,"author")

    for quote, author in zip(quotes, authors):
        all_quotes.append({
            "名言": quote.text,
            "作者": author.text
        })

print("取得件数:", len(all_quotes))
for q in all_quotes[:3]:
    print(q["作者"], ":",  q["名言"][:30])

driver.quit()
