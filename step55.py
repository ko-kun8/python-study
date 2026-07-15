import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1. あなたのGmail設定（※実験用のダミーを入れてあります）
my_email = "ka06bon@gmail.com"   # あなたのGmailアドレス
app_password = "gwpz aamv qmqd nzbd"  # Googleで発行する「アプリパスワード」

# 2. メールの宛先と内容を決める
to_email = my_email #　今回は実験用として「自分宛」におくります

subject = " 【Python自動化テスト）フェーズ３進行中！"
body = "こんにちは！\nこれはpythonのステップ55から自動送信されたメールです"

# 3. メールの「中身の（手紙）」を組み立てる
msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = my_email
msg["To"] = to_email

print("ーーーメール送信処理を開始しますーーー")

try:
    # 4. Gmailの送信サーバー（SMTPサーバー）に接続する
    #    ポート番号「４６５」を使って、安全な通信（SSL）を開始します
    server = smtplib.SMTP_SSL("smtp.gmail.com",465) 

    # 5. あなたのアカウント情報でログインする
    server.login(my_email, app_password) 

    # 6. 【超新技】　メールを実際に送信する！
    server.sendmail(my_email, [to_email], msg.as_string())

    # 7. 終わったらサーバーと接続を綺麗に切断する！
    server.quit()

    print("メールが正常に送信されました！受信トレイを確認してください。")

except Exception as e:
    print(f"エラーが発生しました: {e}")
