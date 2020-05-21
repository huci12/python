#반목문 for

a = "abcdefg"

for i in a :
    print(i)

#순서가 있는 경우

a = ["python" , "java" , "c/c++" , "c#"]

for i in a:
    print(i)


for i in range(100):
    print(i)

#100 미만 까지 찍는다.

for i in range(2,5):
    print(i)

for i in range(1,10,2):
    print(i)

a = [(1,2) , (3,4) , (5,6)]

for i in a :
    for j in i:
        print(j)


#구구단을 빼먹을수 없지

for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))


student = [{"홍길동" : 100} , {"가제트" : 200} , {"가가멜" : 300}]

for i in student:
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("이름 : {} , 점수 : {}".format(name,value))


for s,i in enumerate(student,start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{}.이름 : {} , 점수 : {}".format(s,name,value))


msg = "python programing"


for s,i in enumerate(msg , start=1):
    print("{}.{}".format(s,i))


result = []

for num in range(1,6):
    result.append(num+5)

print(result)

result = [num+5 for num in range(1,6)]
print(result)

result = [num+0 for num in range(1,100) if num % 2 == 0]
print(result)

for num in range(1,99):
    if num%2 == 0:
        result.append(num)

print(result)

#컨프리행션 와
gugudan = ["{} * {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]

print(gugudan)