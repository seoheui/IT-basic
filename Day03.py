"""
    Day03 : Operator, str.format
    Artist
    Date : 2022.10.28
"""

from color import *
cprint("operator")
print('10 > 2 and 10 <20 :', 10> 2 and 10 < 20)
print('10 > 2 and 10 <20 and 3 < 5 :', 10> 2 and 10 < 20 and 3 < 5)
print('3 < 4 < 5', 3 < 4 < 5)
print('10 != 0 or 10 > 100 :', 10 != 0 or 10 > 100)
print('not 10 != 3 :',not 10 != 3)
print()


cprint('str.format()')
print('{}은 또 하나의 {}함수 {}입니다.'.format('이것','print','사용법'))
kor = 10
math = 20
print(f'오늘 아버지가 화나셨습니다. '
      f'이유는 국어{kor}점, 수학 {math}점이기 때문입니다.')
print()


cprint('if statement')
print('**** a = 1 ****')
a = 1
if a > 0 :
      print('a is positive')
elif a == 0:
      print('s is zero')
else :
      print('a is negative')


a = -100
if a > 0 :
      print('a is positive')
      # print('a is positive2') #파이썬은 들여쓰기가 매우 중요
     # print('a is positive3') # 윗줄보다 들여쓰기 레벨이 높아도 안됨
print('a is positive4')

#한 줄로 모든 것을 표현하고자 하는 경우
if a < 0 : print('a is negative5');print("a is negative6") # 옆으로 갔다는 것을 그 라인만 쓰겠다는 것


# 삼항조건문
score = 99
baddad = score > 99 and "당연한 점수" or "어떻게 이렇게 못할수가"
print("아빠의 반응 : ", baddad)
# cf) (score > 99)? "당연" : "그것도점수냐" in C, Java
if score > 99:
      baddad = "당연한 점수"
else:
      baddad = "어떻게 이렇게 못할수가"  #대체가능해서 삼항연산자를 잘 안씀. 그래서 잘 모른다.


