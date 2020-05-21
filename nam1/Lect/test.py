#현재 시간이 12시면 점심을 먹고 아니면 일을 한다
#3시부터 4시까지는 휴식 아니면 아프면 휴식하고
# 일한다
time = 12
seek = True

if time == 12:
    print("점심 먹으러감")
else :
    print("일하는 중")


if time != 12:
    print("일하는중")
else:
    print("밥머겅")


if time >=12 and time < 1:
    print("일행")
else:
    print("밥머겅")

if 12 <= time < 1:
    print("일하는 중..")
elif 3 <= time <= 4:
    print("휴식행")
else:
    print("밥 머겅")


if 12 <= time < 1 and not seek:
    print("밥머겅")
elif 3 <= time <=4 or seek:
    print("휴식시간")
else:
    print("일행")


a = 10
if a > 10:
    ret = 100
elif a == 10 :
    ret = 200
else:
    ret = 500
print(ret)
ret = 100 if a > 10 else 500
print(ret)


ret = {a > 10 : 100 , a < 10 : 0}.get(True,200)
print(ret)
ret = {True : 100 , False : 500}.get(True , 200)
print(ret)
#이거 신기하네 이거 좀 공부 해보자

name = "abcdef"
if "a" in name:
    print("있음")
else:
    print("없음")



name = ["홍길동","가가멜","가제트"]

if "가제트" not in name :
    print("없음")
else: 
    print("있음")



