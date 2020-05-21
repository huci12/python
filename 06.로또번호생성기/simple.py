import random

count = int(input("로또 번호를 몇개 생성 할가요"))

for j in range(count):
    lotto = []

    rand_num = random.randint(1,46)

    for i in range(6) : 
        while rand_num in lotto :
            rand_num = random.randint(1,46)
        lotto.append(rand_num)

    lotto.sort()

    print("{}.로또번호 : {}".format(j+1,lotto))