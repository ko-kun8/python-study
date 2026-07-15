import time
import pyautogui # 🌟新顔：マウスとキーボードを操る自動化のプロ

# 人間が慌てないように、3秒間カウントダウンして待つ
time.sleep(3)

try:
    # 1. 今の画面の横幅と縦幅（解像度）を調べる
    width,height = pyautogui.size()
    print(f"✅ あなたの画面のサイズ: 横 {width} ピクセル × 縦 {height} ピクセル")

    # 2. 画面の「ちょうど真ん中」の座標（XとY）を計算する
    center_x = width // 2
    center_y = height // 2

    # 3. 【大サビ】マウスを画面の真ん中へ「2秒」かけて自動で移動させる！
    print(f"🚀 マウスを画面中央（X:{center_x}, Y:{center_y}）へ自動移動します...")
    pyautogui.moveTo(center_x, center_y, duration=2.0)

    # 4. 移動した先で、自動で「右クリック」を1回ポチッと押す！
    print("👉 画面中央で右クリックを実行します！")
    pyautogui.rightClick()

except Exception as e:
    print(f"エラーが発生しました: {e}")

print("ーーー GUI操作の自動化テストが完了しました ーーー")