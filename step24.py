import re

# 基本の検索
text = "私の電話番号は090-1234-5678です"
result = re.search(r"\d{3}-\d{4}-\d{4}", text)
if result:
    print("見つかった:", result.group())

# 全部取り出す
text2 = "りんご100円、バナナ200円、みかん150円"
numbers = re.findall(r"\d+", text2)
print("数字一覧:", numbers)

# 置換する
text3 = "今日は2026/05/19です"
result2 = re.sub(r"\d{4}/\d{2}/\d{2}", "〇〇〇〇/〇〇/〇〇", text3)
print(result2)

# メールアドレスを抽出
text4 = "連絡先はtest@example.comまたはinfo@test.co.jpです"
emails = re.findall(r"[a-zA-Z0-9.]+@[a-zA-Z0-9.]+", text4)
print("メール:", emails)