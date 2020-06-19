import random
import math
hand=["グー","チョキ","パー","ゲーム終了"]

print("じゃんけん開始")
score=0
count=0

while True:
    try:
        if count>0:
            win=math.floor(score/count*100)
            print(count,"戦目")
            print("スコア:",score,"/",count)
            print('勝率',win)
        com=random.randint(0,2)

        for i,name in enumerate(hand):
          print(i,name)
        you = int(input("出す手を数値で入力:"))
        if you ==3:break
    except:
      print("0から3の間で入力してください")
      continue
    print("-----")
    print("自分",hand[you])
    print("相手",hand[com])
    input("-----")
    j=(you-com+3)%3
    if j==0:
      print("あいこ")
    elif j==1:
      print("負け")
      count+=1
    else:
      print("勝ち")
      count+=1
      score+=1
    input("-----")
