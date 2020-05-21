#데코레이터
#이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

#파이썬에서 함수는 일급객체
#클로저 사용
#함수내 함수를 정의 할수 있음

def outer_function(msg):
    def inner_function():
        return "나는 내부 함수인데 {} 메세지를 받았어".format(msg)
    return inner_function

c = outer_function("헬로")


#print(dir(c))

#print(c())

#print(type(c.__closure__))

#print(len(c.__closure__))

#print(dir(c.__closure__[0]))

#print(c.__closure__[0].cell_contents)


#클로져 사용방법

import time
from functools import wraps

def time_checker(func):
    def inner_function(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print("함수 {} 동작시간: {}".format(func.__name__,end_time-start_time))
        return result
    return inner_function

@time_checker
def test1():
    for i in range(5):
        time.sleep(0.1)

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

test1()
test2()


def test():
    start_time = time.time()
    for i in range(5):
        time.sleep(0.1)
    end_time = time.time() - start_time
    print("함수 동작 시간 : {}".format(end_time))


#test()

# @wraps function으로 넘어온 docString을 사용한다.
def login_required(func):
    @wraps(func)
    def inner_function(*args,**kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 되지 않아 수행 하지 못합니다.")
            return "로그인이 필요한 페이지 입니다."
        return func(*args,**kwargs)
    return inner_function

#로그인의 inner function 조건을 만족하지 못한다.
@login_required
def login():
    '''로그인 테스트 함수 입니다.'''
    print("안녕")

# @ 데코레이트가 들어가게 되면 ''' 이거 안나온다
# 사용 할려면 from functools import wraps
print(login.__doc__)
print(login.__name__)
login()

def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}>{}</{}>".format(new_args,func(name),new_args)
        return wrapper
    return decorator


@add_tag("html")
def testMsg(msg):
    return "방가워" + msg

print(testMsg("홍길동"))
