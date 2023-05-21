def check_score(tensu):
    if int_tensu == 100:
        print("今日はご褒美上げましょう！おめでとうございます！！！")
    elif int_tensu >= 90 and  int_tensu <= 99:
        print("すごいですね！！評価は優です")
    elif int_tensu >= 89 and  int_tensu <= 70:
        print("良い感じです！評価は良です")
    elif int_tensu >= 30 and  int_tensu <= 69:
        print("上を目指して頑張りましょう！評価は可です")
    elif int_tensu >= 10 and  int_tensu <= 29:
        print("勉強不足です！評価は不可です")
    elif int_tensu >= 0 and int_tensu <= 9:
        print("一時間自習してください")
    else:
        print("0 ~ 100の間で入力をしてください")

def is_digit(str):
    for i in range(len(str)):
        if "0" <= str[i] and str[i] <= "9":
             continue
        else:
            return False
    return True

count = 0
while count < 5:
    str_score = input("点数を入力してください")
    if is_digit(str_score):
        int_tensu = int (str_score)
        check_score(int_tensu)
    else:
        print("数値を入力してください")
        continue
    count += 1
print("お疲れさまでした")