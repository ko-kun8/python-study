import os
from pypdf import PdfWriter  # 🌟 PdfWriter に変更します

# 1. PDFが置いてあるフォルダと、合体後のファイル名を決める
target_folder = "自動化テストフォルダ"
output_pdf_path = os.path.join(target_folder, "合体したファイル.pdf")

# 2. PDF合体ロボ（Merger）を起動する
merger = PdfWriter()

print("ーーー PDFの結合処理を開始します ーーー")

try:
    # 3. フォルダの中にあるファイルを1個ずつチェック
    for file_name in os.listdir(target_folder):
        
        # もし最後が「.pdf」で終わるファイルなら
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(target_folder, file_name)
            
            # 合体ロボにPDFを読み込ませる（追加する）
            merger.append(pdf_path)
            print(f"📄 {file_name} を合体リストに追加しました。")
            
    # 4. 【超新技】すべてを合体させた新しいPDFファイルを書き出す！
    merger.write(output_pdf_path)
    
    # 5. 使い終わった合体ロボをお片付け（閉じる）
    merger.close()
    
    print(f"✨ 結合が完了しました！➔ {output_pdf_path}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")