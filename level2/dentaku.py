import sys

def calculate(num1, operator, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
       print("数値以外が入力されました")
       sys.exit(1)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
       if num2 ==0:
           print("oで割ることはできません")
           sys.exit(1)
       result = num1 / num2 
    
    else:
        print('無効な演算子です。')
        sys.exit(1)

    print("Result: ", result)

if __name__ == '__main__': 
    if len(sys.argv) != 4:
        print('引数の数が正しくありません。')
        sys.exit(1)

    num1 = None
    try:
         num1 = float(sys.argv[1])
    except ValueError:
         print("Error: 数値以外が入力されました。")
         sys.exit(1)
                 
    operator = sys.argv[2]

    num2 = None
    try:
         num2 = float(sys.argv[3])
    except ValueError:
         print("Error: 数値以外が入力されました。")
         sys.exit(1)

    calculate(num1, operator, num2)


