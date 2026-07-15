from platform import python_branch
import time
import pyautogui

print("ーーー ブラウザ操作応用テストを開始します ーーー")
print("⚠️ 3秒後にスタートします。ブラウザ（Chromeなど）を画面いっぱいに開いておいてください！")

# 人間が準備するための待ち時間
time.sleep(3)

try:
    # 1. まずブラウザの「アドレスバー（URLを入れるところ）」あたりを狙って自動クリック
    # ※一般的なパソコンの画面上部（X:500, Y:80）あたりを仮のターゲットにします
    print("🚀 ブラウザの上部（アドレスバー付近）をクリックします...")
    pyautogui.click(500, 80)
    time.sleep(1)

    # 2. 【大サビ1】検索したい文字を自動でタイピング！
    # ※pyautoguiは標準では日本語が苦手なため、まずは英語で「python」と打たせます
    print("⌨️ 検索ワード 'python' を自動入力中...")
    pyautogui.write("python", interval=0.1) # interval=0.1 で人間が打っているように0.1秒ごとに入力
    time.sleep(1)
    
    # 3. 【大サビ2】キーボードの「Enter」キーを自動でガツンと押す！
    print("Enterキーを押し下げて検索を実行します！")
    pyautogui.press("enter")

except Exception as e:
    print(f"エラーが発生しました: {e}")

print("ーーー ブラウザ操作応用テストが完了しました ーーー")

