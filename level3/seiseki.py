tensu = input("点数を入力してください:")
int_tensu = int(tensu)
#if int_tensu == str(tensu):
   # except ValueError:
       # print = ("数値以外が入力されています。正しい値を入力してください。")

if int_tensu <0 or int_tensu >100:
    print("0~100の範囲外の数字が入力されました。正しい値を入力してください。")
   
count = 0

while count <6:
    user_input = input("点数を入力してください:")

    if int_tensu ==100:
        print("今日はご褒美上げましょう！おめでとうございます！！！")
    elif int_tensu >= 90 and  int_tensu <= 99:
        print("すごいですね！！評価は優です")
    elif int_tensu >= 89 and  int_tensu <= 70:
        print("良い感じです！評価は良です")
    elif int_tensu >= 69 and  int_tensu <= 69:
        print("上を目指して頑張りましょう！評価は可です")
    elif int_tensu >= 29 and  int_tensu <= 10:
        print("勉強不足です！評価は不可です")
    elif int_tensu ==0:
        print("一時間自習してください")

    count += 1
    if count == 6:
        print("入力完了です。ありがとうございました。")
        break
