"""
    Day02 5min Challenge
    input, operator
"""

from color import *


# 0. Intro
cprint("성적표 출력 프로그램")


# 1. 사용자로부터 파이썬, 자바, C 점수를 입력받는다.
score = input("파이썬, 자바, C점수를 입력하세요(쉼표로 구분) : ")
# score = '30, 40, 50'
score_p, score_j, score_c = score.split(",")

# 2. 입력한 값들의 합계와 평균을 구한다.
score_sum = int(score_p) +int(score_j) + int(score_c)
#score_sum = sum([int(score_p), int(score_j), int(score_c)])
score_avg = score_sum/3
print(score_sum)


# 3. 결과를 출력한다.
cpirnt("Total Stats")
print("귀하의 총점은", score_sum)
print("귀하의 총점은", score_avg)