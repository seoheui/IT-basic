from color import *

cprint("Input Test")

# a = input('값을 입력하세요 :')
# print(a)
# b =int(a)+10 # ; 문장을 끊는 부호
# print('변경된 너의 점수는',b)


# difficulty up - multiple input - 스플릿 함수 사용법
# question = "국영수 점수를 입력하세요(쉼표로 구분하여):"
# a, b, c, = input(question).split(',')
# print('너의 국영수 점수는 :', a, b, c)

# more up
# question = "모든 과목 점수를 입력하세요(공백으로 구분하여) : "
# a = input(question).split(' ')
# print('너의 모든 과목 점수는 :', a)

print("")
cprint("Operator")
print("(1)산술연산자")
a = "I'll be "
b = 100
print(a +str(b))

print("10-10,9 = ", 10 - 10.9)  #파이썬이 소수점 아래 여섯번째부터는 정확성을 보장하지 않음
print("안녕"*10)
#print("###"/"#") # 오류
#print(10/0) # 오류

print("10//3 = ", 10//3)
print("10 % 3 = ", 10%3)
print("5**1.5 = ", 5**1.5)
print(" ")

print("(2) 관계연산자")
a = 30
b = 20
c = a>b
print(c)
print(type(c))
c = 10
print(type(c))
print( (10 != 20) != False) # ==, !=는 매우 중요
