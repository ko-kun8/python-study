def calculate_tax(price_text):
    print("--- デバッグ開始 ---")
    print(f"受け取った値: {price_text} (型: {type(price_text)})")
    
    # 💡 文字列から整数（int）に変換します！
    price_number = int(price_text)
    
    # 数字に変わったので、無事に掛け算ができるようになります
    tax = price_number * 0.1
    return tax

# 実行してみる
price = "1000"
print(calculate_tax(price))