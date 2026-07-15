from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 1. PDFの保存名（ファイル名）を決める
filename = "sample.pdf"

# 2. まっさらなPDFの「キャンバス（画用紙）」を用意する
c = canvas.Canvas(filename)

# 3. 大事！日本語を使えるようにフォントを登録する（今回は明朝体）
font_name = "HeiseiMin-W3"
pdfmetrics.registerFont(UnicodeCIDFont(font_name))

# 4. 文字のフォントと大きさを指定する（フォント名, サイズ）
c.setFont(font_name, 24)

# 5. 画用紙に文字を書く（左からの距離, 下からの距離, 書く文字）
# ※PDFの世界では、左下隅が「0, 0」のスタート位置になります
c.drawString(100, 700, "PythonでPDFを作りました！")

c.setFont(font_name, 14)
c.drawString(100, 650, "これは、pdfplumberの練習に使うためのサンプルPDFです。")
c.drawString(100, 620, "無事に読み込めるかテストしてみましょう。")

# 6. 画用紙に「線を引く」こともできます（スタートのX, Y, ゴールのX, Y）
c.line(100, 600, 500, 600)

# 7. 書き込みを終了して、PDFとして保存する
c.showPage()
c.save()

print(f"{filename} を作成しました！")