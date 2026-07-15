import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 🌟新顔：合体ロボ
from email.mime.base import MIMEBase            # 🌟新顔：ファイル担当
from email import encoders                      # 🌟新顔：暗号化担当
import os

# 1. あなたのGmail設定（さっきの正しい情報に書き換えてください！）
my_email = "ka06bon@gmail.com"
app_password = "gwpz aamv qmqd nzbd"
to_email = my_email  

# 2. 添付したいファイルの場所（今回はテキストファイルフォルダの中身を狙います）
# ※もしファイル名が違う場合は、実際のファイル名に合わせて書き換えてください！
file_path = os.path.join("自動化テストフォルダ", "テキストファイル", "【自動化】test.txt")
file_name = os.path.basename(file_path)

# 3. 【超新技】「本文」と「添付ファイル」を両方詰め込める魔法のバッグ（MIMEMultipart）を作る
msg = MIMEMultipart()
msg["Subject"] = "【Python自動化テスト】ファイルを添付して送信！"
msg["From"] = my_email
msg["To"] = to_email

# 4. まずは「本文」をバッグに入れる
body = "こんにちは！\n\nPythonを使って、ファイルを添付したメールの自動送信テストです。"
msg.attach(MIMEText(body, "plain", "utf-8"))

print("ーーー メールの組み立てと送信を開始します ーーー")

try:
    # 5. 【超新技】ファイルを読み込んでバッグに詰め込む処理
    if os.path.exists(file_path):
        # ファイルをバイナリ（データそのもの）として開く
        with open(file_path, "rb") as f:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(f.read())
        
        # ネットで送れるようにデータをエンコード（変換）する
        encoders.encode_base64(attachment)
        
        # 封筒に「これはファイルですよ」という名前（ヘッダー）をつける
        attachment.add_header("Content-Disposition", f"attachment; filename={file_name}")
        
        # バッグにファイルを合体させる！
        msg.attach(attachment)
    else:
        print("⚠️ 添付するファイルが見つかりませんでした。住所を確認してください。")

    # 6. いつもの手順で送信所に接続して送る
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(my_email, app_password)
    server.sendmail(my_email, [to_email], msg.as_string())
    server.quit()
    
    print("✨ ファイル付きメールが正常に送信されました！")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")