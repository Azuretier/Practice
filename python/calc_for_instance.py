# input()とインスタンスを使用した計算機

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2
    
    def devide(self):
        return self.num1 / self.num2

while True:

    # 任意の整数を入力させる
    num1 = input("num1: ")

    # "end"と入力した場合はループを終了
    if num1 == "end":
        break

    num2 = input("num2: ")

    # "end"と入力した場合はループを終了
    if num2 == "end":
        break

    math_method = input("math_method: ")

    # "end"と入力した場合はループを終了
    if math_method == "end":
        break

    try:

        # 入力された整数をintに変換
        num1 = int(num1)
        num2 = int(num2)
        calc = Calculator(num1, num2)

        if math_method == "add":
            result = calc.add()

        elif math_method == "substract":
            result = calc.substract()

        elif math_method == "multiply":
            result = calc.multiply()

        elif math_method == "devide":
            result = calc.devide()

        else: 
            print("有効な計算方法を入力してください。")

    except ValueError:

        # エラーハンドリング
        print("有効な整数を入力してください。")

    print(f"result: {result}")