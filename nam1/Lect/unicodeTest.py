a="가"
print(a.encode("utf-8"))
print(a.encode("cp949"))
print(ord(a))
print(hex(ord(a)))
print(bin(ord(a)))


file = open("utf8.txt" , mode = "w" ,encoding="utf-8")
file.write(a)
file.close()


file = open("utf8.txt" , mode = "rb")
print(file.read())
print(file.read().decode("utf-8"))
file.close()


with open("utf8.txt" , mode = "r" , encoding="utf-8") as s :
    print(s.read())
    


