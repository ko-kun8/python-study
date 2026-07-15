import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Windowsの日本語フォントを使う
plt.rcParams["font.family"] = "MS Gothic"

#データ
names = ["太郎","花子", "次郎", "四郎"]
sales = [100, 150, 80, 200]

#棒グラフ
plt.figure(figsize=(8, 5))
plt.bar(names, sales, color="steelblue")
plt.title("売上グラフ")
plt.xlabel("名前")
plt.ylabel("売上")
plt.savefig("bar_chart.png")
plt.show()
print("bar_chart.png を保存しました！")

#折れ線グラフ
months = ["1月", "２月", "３月", "４月"]
values = [100, 150, 120, 200]

plt.figure(figsize=(8,5))
plt.plot(months, values, marker="o", color="tomato")
plt.title("月別売上")
plt.xlabel("月")
plt.ylabel("売上")
plt.savefig("line_chart.png")
plt.show()
print("line_chart.png を保存しました！")