name = input("名前を入力してください:")
print(name + "さん、今から数当てゲームをおこないます")

import random
target_number = random.randint(1,100)

kazuate = int(input("数字を入力してください:"))
def is_digit(str):
  for i in range(len(str)):
    continue
  else:
    return False
  return True

while True:
  if kazuate < target_number:
    print(str(kazuate) + "はプログラムの数字より小さいです")
  if kazuate > target_number:
    print(str(kazuate) + "はプログラムの数字より大きいです")
  else:
    print("おめでとうございます！正解です！")
    break
