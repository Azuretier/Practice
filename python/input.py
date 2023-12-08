while True:
    # 任意の整数を入力させる
    user_input = input("任意の整数を入力してください: ")

    # "end"と入力した場合はループを終了
    if user_input == "end":
        break

    try:
        # 入力された整数をintに変換
        number = int(user_input)
        # 入力された整数を表示
        print(f"入力された整数は {user_input} です。")

    except ValueError:
        # エラーハンドリング
        print("有効な整数を入力してください。もう一度試してください。")