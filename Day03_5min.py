"""
    Day 5min Challenge
"""

from color import *
print(RED + '***** 초고속 양음수 판독기 *****" + END')

# 1. 사용자로부터 입력을 하나 받는다.(실수)
#Input = input('양수, 0, 음수:')
#positive, zero, negative = Input.split(',')


# 2. 입력한 숫자가 양수, 0, 음수인지를 출력한다.

# 3. 양수면 초록색글자 음수면 빨간색 글자로 표현한다.
#print(GREEN + positive + ',' + RED + negative)

num = input("수를 입력하세요 :")
num = float(num)


if num > 0 :
    print(GREEN + '이거 양수네' + END)
elif num == 0 :
    print('0을 입력해놓고 0인지 모른다')
elif num < 0 :
    print(RED +'음수입니다.' + END)
