import os
from pypdf import PdfReader, PdfWriter  # 🌟新顔：読み込み担当（Reader）も呼び出す

target_folder = "自動化テストフォルダ"
# 元になるPDF（さっき合体させたファイル）
input_pdf_path = os.path.join(target_folder, "合体したファイル.pdf")
# 切り抜いた後の保存先
output_pdf_path = os.path.join(target_folder, "切り抜いた1ページ目.pdf")

print("ーーー PDFの分割（切り抜き）処理を開始します ーーー")

try:
    # 1. 【新技】元になるPDFをじっくり「読み込む」
    reader = PdfReader(input_pdf_path)
    
    # 2. 新しいPDFを書き出すためのバインダー（Writer）を用意
    writer = PdfWriter()
    
    # 3. 【超重要】1ページ目を指定して、新しいバインダーにコピーする
    # ※プログラミングの世界では、1ページ目は「0」番目と数えます！
    target_page = reader.pages[0]
    writer.add_page(target_page)
    
    # 4. 切り抜いたページを新しいファイルとして保存
    with open(output_pdf_path, "wb") as f:
        writer.write(f)
        
    print(f"✨ 切り抜きが完了しました！➔ {output_pdf_path}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")