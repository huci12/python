#파이썬 예외 처리 try/ except



try:
    val = "10.5"
    n = int(val)
except:
    print("오류")


try:
    val = "10.5"
    n = int(val)
except ValueError as e:
    print("오류발생 {}".format(e))

try:
    idx = []
    idx[0] = 100
except IndexError as e:
    print("오류발생 {}".format(e))


try:
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류발생 {}".format(e))
    pass

print("OK")

try:
    n = "10"
    v = int(n)
except:
    print("오류발생")
else:
    print("정상동작")



try:
    files = open("sameple.txt","r")
    n = "10.5"
    v = int(n)
except:
    print("오류발생")
finally:
    files.close()
    print("최종 도착")
    




