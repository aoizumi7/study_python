import sys

def calculate(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print('無効な演算子です。')
        return

    print('計算結果は', result, 'です。')

if __name__ == '__main__':
    print(sys.argv[0]) 
    if len(sys.argv) != 4:
        print('引数の数が正しくありません。')
        sys.exit()

    operator = sys.argv[1]
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])
    calculate(operator, num1, num2)
