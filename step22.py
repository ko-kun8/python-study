from datetime import datetime, timedelta

#k今日の日付を取得
today = datetime.now()
print(today)

#日付のフォーマットを変える
print(today.strftime("%Y年%m月%d日"))
print(today.strftime("%Y/%m/%d %H:%M:%S"))

#日付の計算
tomorrow = today + timedelta(days=1)
print("明日:", tomorrow.strftime("%Y/%m/%d"))

last_week = today - timedelta(days=7)
print("1週間:", last_week.strftime("%Y/%m/%d"))

#文字列を日付に変換
date_str = "2024/01/15"
date = datetime.strptime(date_str, "%Y/%m/%d")
print(date)

#２つの日付の差を計算
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
diff = date2 - date1
print("日数の差:", diff.days, "日")