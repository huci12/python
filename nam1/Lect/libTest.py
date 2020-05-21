#라이브러리


import os
import time
import datetime
import random

#os.getcwd()
#os.system("cls")

#os.rmdir("지울폴더")
#os.listdir("리스트 폴더 목록")

a = time.time()
print(a)

#1초동안 멈춤
time.sleep(1)

d = datetime.datetime.now()

print(d.date())

print(d.time())

print(d.month)
print(d.DAY)

d.strptime()

d.strptime("%c")
d.strptime("%Y")

random.random()

random.randint(1,10000)

l = ["가위","바위","보"]

random.choice(l)

random.shuffle(l)

#외부 라이브러리 설치
#pip install requests
#pip uninstall requests

#현재 설치된 라이브러리 목록을 나타내라
#pip freeze > reqeust.txt

#해당 텍스트의 라이브러리를 설치해라
#pip install -r .\requests.txt


#현재 pip 리퀘스트를 봐라
#pip show reqeusts