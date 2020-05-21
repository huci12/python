# 사용자 함수

def 함수명():
    print("함수 호출")
    return True


a = print(함수명())

def add(a,b):
    global c
    c = a + b
    return c

a = add(1,2)
print(c)

#global은 내부에서 사용하는 지역 변수가 아닌
#전역변수 c라고 생각하면 됩니다.
#마치 자바 클래스의 this. 이것과 비슷한 느낌이네요

#파이썬의 재미 있는점 파라미터 기본값 설정이 가능하여 생략이 가능하다.
def get_input_user(msg , casting=int):
    ''' 사용자에게 값을 받고 주어진 캐스팅을 함 '''
    while True :
        try : 
            user = casting(input(msg))
            return user
        except:
            continue
    





user = get_input_user("사용자 이름을 입력 하세요." , str)


age = get_input_user("사용자 나이를 입력 하세요.")




#보통 지역변수의 경우 외부에 영향을 못미치지만

def test1(num):
    num += 10
    print(num)


a = 100 
print(test1(a))
print(a)

def test2(lists):
    lists.append("AAA")
    
#이런 경우 당연히 변경이 될수 밖에
#call by reference 이기 때문에
#list , dict , set 같은 자료형 ㅇㅇ
#int str 이런건 그냥 call by Value
a = ['1111']

test2(a)

print(a)


#여러개의 파라미턴 포지셔널 파라미터를 받기
#튜플로 받게 된다.
def save_winner(*args):
    print(args)

save_winner("가")
save_winner("가","나")
save_winner("가","나","다")

#딕서녀리 형태로 받음 키워드아규먼트
def save_winner2(**kwargs):
    print(kwargs)


save_winner2(name1="가",name2="나",name3="다")


def hi():
    print("Hello")


hello = hi
hello()

print(type(hello))



def outer_function(func):
    def inner_function(*args,**kwargs):
        print("함수명{}".format(func.__name__))
        result = func(*args,**kwargs)
        return result
    return inner_function
