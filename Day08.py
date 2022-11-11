from color import *

cprint('String Advanced')
s1 = 'my name is messi'
print(s1.find('messi')) # index 11에 위치
print(s1.find('Messi')) # 문자열이 없으면 -1
if s1.find('messi') >= 0:
    print('니 단어 있다')

print('messi' in s1)
if 'messi' in s1:
    print('니 단어 있다.')

print("MESSI".lower() in s1.lower()) #대소문자 구분없이 체크
print(s1.title())

#lstrip, rstrip, strip
s3 = '       I am a Programmer@@@@@@@@1111111@@@@@@rr@1'
s4 = s3.lstrip(' ')
print('원본 :',s3)
print('왼쪽 공백제거 :', s4)
s5 = s4.rstrip('1')
print('오른쪽 처리 :', s5)
s5 = s4.rstrip('r@1') # 오른쪽부터 검사, r @ 1 중의 하나인지, 맞으면 삭제, 안맞을때까지 반복
print('오른쪽 처리2 :', s5) # Rrogrammer에서 r도 없어진다

#String 배열 연습
a = 'abcdefg'
print(a)
print(a[0],a[5]) # a f
print(a[1:3]) # bd
print(a[3:]) # defg
print(a[3::2]) # df
print(a[::-1]) # a를 역순으로 만드는 것
print()

cprint('Array Copy')
a = list(range(1,11))
b = [range(1,11)]
print(a,b)

# b는 a의 index 1부터 끝까지 복사
b = a[1:]
print(b)

c = (1,2,3,4,5)
d = c[1::2]
print(d)

e = {1,2,3,4,5}
f = e #set은 index가 없으므로 전체복사만 가능

#
listA = ['a','b','c']
strA = str(listA)
print("LIve Show :", strA)
print(strA == listA)
print(strA[0])
strB = "abc"
listB = list(strB)
print(listB)
print()

cprint("User (Defined) Function")
#Type1
def printMsg1():
    print("Welcome to my house in Europe")

printMsg1()

# Type 2
def printMsg2(message):
    print(message +" 같은 거 전송하지마")
printMsg2("우리의 고향")
#printMsg2()

def printMsg3(message = "너 빈손일 줄 알았네"):
    print(message)
    if message != "너 빈손일 줄 알았네":
        print("웬일이래")
printMsg3()
printMsg3("뭐라고?")
