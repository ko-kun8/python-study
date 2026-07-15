import os
import openpyxl  # 🌟新顔：Excelを操作する大ボス

target_folder = "自動化テストフォルダ"
excel_path = os.path.join(target_folder, "Pythonで作ったシート.xlsx")

print("ーーー Excelファイルの作成・操作を開始します ーーー")

try:
    # 1. 新しいExcelブックを白紙の状態で作成
    wb = openpyxl.Workbook()
    
    # 2. 現在開いているアクティブなシート（Sheet）を選択
    sheet = wb.active
    sheet.title = "自動化テスト"  # シートの名前を「自動化テスト」に変更
    
    # 3. 【書き込み】A1マスとA2マスに文字を書き込む！
    sheet["A1"] = "項目名"
    sheet["A2"] = "Pythonからこんにちは！"
    print("✍️ ExcelのA1、A2マスに文字を書き込みました！")
    
    # 4. 【読み込み】書き込んだA2マスの内容を読み込んで画面に出してみる
    a2_value = sheet["A2"].value
    print(f"📖 読み込んだA2マスの値: {a2_value}")
    
    # 5. 指定した場所に名前をつけて保存する
    wb.save(excel_path)
    print(f"✨ Excelファイルの作成が完了しました！➔ {excel_path}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")