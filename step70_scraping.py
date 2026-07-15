import os
import sys
import requests  # 🌟新顔1：WEBページをダウンロードする部隊
from bs4 import BeautifulSoup  # 🌟新顔2：欲しい文字を綺麗に切り抜くスープ職人

# 🌟魔法の1行：どこから起動されてもファイルを見失わないようにする
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print("ーーー Webスクレイピング実践テストを開始します ーーー")

# 1. データを引っこ抜きたいテスト用のウェブサイトのURL
url = "http://books.toscrape.com/"

try:
    print(f"🌐 ターゲットのサイト（{url}）に接続中...")
    
    # 2. 【大サビ1】requestsを使って、ウェブサイトのデータを丸ごとダウンロードする
    response = requests.get(url)
    
    # 3. BeautifulSoupを使って、ダウンロードしたデータをPythonが読める形に解凍・調理する
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. 【大サビ2】ページ内にある「本の一覧（h3タグ）」をすべて探し出す！
    # ※WEBサイトの裏側にある「h3」という目印を狙い撃ちします
    book_titles = soup.find_all("h3")
    
    print(f"✅ サイトへの接続に成功！ 本を {len(book_titles)} 冊見つけました。")
    print("\n📚 ーーー 見つかった本のタイトル一覧 ーーー")
    
    # 5. 見つかった本を、forループで1冊ずつ画面に表示する
    for book in book_titles:
        # aタグ（リンク）の中に書かれている本の本名を抜き出す
        title_text = book.find("a").get("title")
        print(f"📖 {title_text}")
        
except Exception as e:
    print(f"❌ スクレイピング中にエラーが発生しました: {e}")

print("\nーーー Webスクレイピング実践テストが完了しました ーーー")