# 任意の数字を入力させる
user_input = input("任意の数字を入力してください: ")

try:
    # 入力された数字をfloatに変換
    number = float(user_input)
    # 入力された数字を表示
    print(f"入力された数字は {number} です。")

except ValueError:
    # エラーハンドリング
    print("有効な数字を入力してください。")