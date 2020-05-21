#계산기 만들기
import os

operator = ["+","-","*","/","="]

def string_calculator(user_input,show_history=False) :
    string_list = []
    lop = 0
    for i,s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() !="":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i+1

    if lop < len(user_input) :
        string_list.append(user_input[lop:len(user_input)])

    print(string_list)

    #['10', '+', '20', '+', '30']
    #['10', '+', '20', '+', '30']
    #['30', '+', '30']
    #['60']

    pos = 0
    while True :
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos-1] + string_list[pos] + string_list[pos + 1]
            del string_list[0:3]
            string_list.insert(0,str(eval(temp)))
            pos = 0
            if show_history :
                print(string_list)
        pos += 1
        
    if len(string_list) > 0 :
        result = float(string_list[0])
    return round(result,4)


while True :
    user_input = input("계산식을 입력 하세요.>")
    if user_input == "/exit":
        break
    result = string_calculator(user_input,True)
    print("결과 : {}".format(result))
    os.system("pause")
    os.system("cls")
