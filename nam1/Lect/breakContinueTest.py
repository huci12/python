# while , for

num = 0

while True : 
    print(num)
    num += 1

    if num == 10 : 
        break


for i in range(1,1000):
    print(i)
    if i == 10:
        break



num = 0

while num < 10 :
    num +=1
    if num == 5 :
        continue
    print(num)


point = [80,100,50,40,60]

for p in point : 
    if p < 70 :
        continue
    print(p)