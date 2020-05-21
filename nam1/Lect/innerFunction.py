#내장함수

#파이썬에서 제공하는 다양한 기능들

#int는 모두 10진수를 표현한다
print(int("100")) 

#16진수 100을 변환
print(int("100" , 16))

#8진수 100을 변환
print(int("100" , 8))

#2진수 100을 변환
print(int("100" , 2))


print(float("10.1"))

#0.30000000000000004 
print(0.1+0.2)

#부동소주점의 방식 때문에 0.3이 나오지 않는다.
#이런 언어적 특성때문에
# import math
# math.isclose(0.1+0.2,0.3)

a = 0.1 + 0.2

x,y = a.as_integer_ratio()
print(x,y)
print(a == x/y)

a = "홍길동,김길동,가가멜"
print(a.split(","))

a = a.replace("홍길동" , "박길동")

print(a)

dir(str)

help(str.split)


a = -1
print(abs(a))

print(sum([1,2,3,4,5,6]))

print(all([True,True]))

print(all([0,1]))

print(any([0,1]))

print(any([0,0]))

#unicode 해당하는 값의 문자를 넘겨준다.
print(chr(44032))
#반대로
print(ord('가'))
#2진수
print(bin(44032))

print(bin(10))
#8진수
print(oct(44032))
#16진수
print(hex(10))

a = 10

#첫번째 들어간 변수가 두번째 파라미터의 타입이냐
print(isinstance(a, int))

a = 1/3

print(round(a))

print(round(a,3))