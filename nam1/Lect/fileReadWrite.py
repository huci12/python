#파일 읽고 쓰기

file = open("sample.txt" , mode = "w" ,encoding="utf-8")
#이렇게 유니코드로 적으면 메모장에는 정상적으로 들어갈지라도 기본 인코딩이 ANSI로 되어 있다.
#다른 뷰어에서는 깨질수 있다.
#그래서 encoding 옵션을 넣어주자
file.write("안녕 파이썬")
file.close()


readfile = open("sample.txt" ,mode = "r" , encoding="utf-8")
content = readfile.read()
readLine = readfile.readline()
readfile.close()
print(content)


readfile = open("sample.txt" ,mode = "r" , encoding="utf-8")
#10글자씩 읽기
a = readfile.read(10)
print(readfile.tell())
readfile.seek(0)
#읽어왔던 포인터를 이동
print(readfile.tell())
print(a)
a = readfile.read(10)
print(a)

for l in readfile:
    print(l)
readfile.close()


#with 저기서 file은 변수가 된다. with문을 다 쓰고 빠져나가면 file 객체는 자동 소멸 되서 close 안해도 된다.
with open("sample.txt" , mode="r" , encoding="utf-8") as file:
    print(file.read())


with open("sample.txt" , mode = "r" , encoding="utf-8") as s , open("sample2.txt",mode="w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬","Python"))

with open("sample.txt" , mode = "r" , encoding="utf-8") as s, \
    open("sample2.txt",mode="w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬","Python"))

with open("sample2.txt" , mode="r" , encoding="utf-8") as file:
    print(file.read())