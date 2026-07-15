import os 
from PIL import Image # 新顔：画像を自由自在に操る大ボス

target_folder = "自動化テストフォルダ"
output_folder = os.path.join(target_folder, "リサイズ済み画像")

# 保存先のフォルダがまだなければ、自動で作る
os.makedirs(output_folder, exist_ok=True)

print("ーーー画像の一括変換（サイズ縮小）を開始しますーーー")

try:
    # 1. フォルダの中にあるファイルを1個ずつチェック
    for file_name in os.listdir(target_folder):

        # 小文字にして変換して、拡張子が .jpg, .jpeg, .png のどれかだったら処理する
        if file_name.lower().endswith((".jpg", ".jpeg", "png")):
            image_path = os.path.join(target_folder, file_name)

            # 2. 【新技】画像を開く
            with Image.open(image_path) as img:

                # 3. 【超重要】横幅を【400ピクセル】にして縦横の比率を保ったまま縮小する
                # (400,400)などのサイズを自動計算してくれます
                img.thumbnail((400,400))

                # 4. 新しいフォルダに同じ名前で保存する
                save_path = os.path.join(output_folder, file_name)
                img.save(save_path)

                print(f"{file_name}を小さくして保存しました！")

    print(f" すべての画像処理が完了しました！→{output_folder}を見てね")

except Exception as e:
    print(f" エラーが発生しました: {e}")
    
