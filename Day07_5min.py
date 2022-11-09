"""
    Day 7 Challenge
    Calculator for Engineering
"""
"""
    0. Opening
    1.무한루프로 사용자에게 수식을 입력받는다.
    2. 수식 대신 'X'를 입력하면 종료된다.
    3.수식을 계산하여 수식과 결과를 출력한다.
      결과는 총 40칸, 우측 정렬하여 출력
    4.사용자가 수식을 계속하여 입력하면 기존의 수식들을 출력하고 기존 결과에 추가로 수식을 계산한 결과를 출력한다.
    5.수식 대신에 'C'를 입력하면 0을 출력하고 수식들을 다 비운다.
"""
from color import *
# 0. Opening
cprint("Calculator for Engineering")

exp_list = []
res = ""

#1.무한루프로 사용자에게 수식을 입력받는다. X를 입력하면 종료한다.
while True:
    exp = input('수식을 입력하세요(종료는 "X",초기화는 "C"):' )
    if exp == 'X':
        break
    elif exp == 'C':
        print(0)
        exp_list.clear()
        res = ""
        continue

    # 수식을 계산한다.
    res = eval(str(res)+ " " + exp)

    exp_list.append(exp)
    #수식을 출력한다
    print(exp_list)
    for idx, exp in enumerate(exp_list):
        if idx == len(exp_list)-1:
            print("\033[1m" +"\033[4m"+ RED + format(exp,'>40') + END) #ANSI escape code, ESC =\033
        else:
            print(GREEN + format(exp,'>40') + END)

    # 결과를 출력한다.
    print(YELLOW + "-"*40 +END)
    print(format(res,'>40'))

    print(res)
