#입력값 받기 
'''
user = input("사용자 이름 입력 하세요.")
print(user)


num1 = int(input("숫자1"))
num2 = int(input("숫자2"))
print(num1 + num2)
'''


# langs = ["kor","eng"]

# for s,i in enumerate(langs,start=1):
#     print("{} . {}".format(s,i))

# while True :
#     sel = input("언어를 선택 하세요")
#     if not sel.isnumeric():
#         continue
#     if 0 < int(sel) < 3:
#         break

# print("사용자가 선택한 언어는{}".format(langs[int(sel)-1]))
    

# while True:
#     num = input("2 이상의 숫자를 입력하세요 > ")
#     if not num.isnumeric():
#         continue
#     num = int(num)
#     if num < 2:
#         continue
#     break

# num = int(input("2 이상의 숫자를 입력하세요 > "))
# isPrime = True
# for n in range(2,num):
#     if num % n == 0 :
#         isPrime = False
#         break
# if isPrime:
#     print("소수임")
# else:
#     print("소수가 아님")


num = int(input("2 이상의 숫자를 입력하세요 > "))
prime_list = [False,False] + [True] * (num - 1)
print(prime_list)
primes = []
#ragne(start,end,step)
for i in range(2,num + 1):
    if prime_list[i]:
        for j in range(2 * i , num + 1 ,i):
            prime_list[j] = False

primes = [i for i in range(2,num+1) if prime_list[i] == True]
print(primes)

if num in primes:
    print("소수 입니다.")
else : 
    print("소수가 아님")