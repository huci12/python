#정해진 숫자를 맞추면 원스트라이크
#틀리면 볼
#스트라이크 3개 아웃 볼 4개 진출

import random 
numbers = []
number = 0
for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)
count_strike = 0
count_ball = 0
# 1 , 2 , 3
while count_strike < 3 :
    num = str(input("숫자 3 자리를 입력 하세요"))
    if len(num) == 3:
        for i in range(0,3):
            for j in range(0,3):
                if num[i] == numbers[j] and i == j :
                    count_strike += 1
                elif num[i] == numbers[j] and i != j :
                    count_ball +=1
        if count_strike == 0 and count_ball == 0 :
            print("3 아웃")
        else:
            output = ""
            if count_strike > 0 : 
                output+= "{}스트라이크".format(count_strike)
            if count_ball > 0 :
                output+= "{} 볼".format(count_ball)

            print(output)

print("게임 성공")