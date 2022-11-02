"""
    Day4 5min Challenge
"""
"""
    1. '이름을 입력하세요"'를 출력하고 이름을 받는다.
    2. '최대숫자를 입력하세요:'를 출력하고 정수로 입력을 받는다.
    3. 1부터 최대 숫자 사이의 수를 하나 랜덤으로 얻는다.
    4. 숫자 입력을 받아 임의의 수와 같은지 맞추는 게임을 한다.
        정답은 몇일까요?를 출력하고 입력을 받는다.
        임의의 수와 입력한 수가 같으면 종료한다.
    5. 결과에 따라 출력한다.
        한번에 맞추면 "***님 대단하십니다"
        세 번 이내에 맞추면"***님 우수한 성적이십니다"
        다섯 번 이내에 맞추면 "***님 그저 그렇습니다."
        다섯 번까지도 못 맞추면 "넌 뭐냐? 정답은 **다"
"""
#1
nam = input("이름을 입력하세요 :")
#2
while True:
    num = input("최대 숫자를 입력하세요 :")
    if num.isdecimal():
        num = int(num)
        break
    else:
        print("니가 뭘 입력했는지 봐봐")
#3
import random
rand_num = random.randint(1, num)
print(rand_num)
#4
n=1
while True:
    answer = int(input('정답은 몇일까요? :'))
    if answer == rand_num:
        break
    else:
        n = n + 1
    if n > 5 :               #boundary test 5일때 정답안, 6일때 정답 밖
        break

#5
if n == 1:
    print(nam + '님 대단하싶니다')
elif n <= 3:
    print(nam + '님 우수한 성적이십니다')
elif n <= 5:
    print(nam + '님 그저 그렇습니다')
else:
    print(f'넌 뭐냐? 정답은{rand_num}이다.')


