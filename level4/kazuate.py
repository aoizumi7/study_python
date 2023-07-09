name = input("名前を入力してください:")
print(name + "さん、今から数当てゲームをおこないます")

import random
target_number = random.randint(1,100)

while True:
  kazuate = int(input("数字を入力してください:"))
  #if kazuate <0  or kazuate >100:
  #print("1以上100以下の数字を入力してください")

  if kazuate < target_number:
    print(str(kazuate) + "はプログラムの数字より小さいです")
  if kazuate > target_number:
    print(str(kazuate) + "はプログラムの数字より大きいです")
  else:
    print("おめでとうございます！正解です！")
    break
