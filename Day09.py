from color import *

cprint('User Function - 2')

# type - return : cf) C,Java : int, float, void
def getRandomDice(i=6):
    import random
    r = random.randint(1,i)
    return r

basket = getRandomDice(100)
print(basket)

# type -return multi-value
def getPizzaPiece():
    import random
    i = random.randint(1,8)
    j = random.randint(0,8-i)
    k = 8-i-j
    return i, j, k

james, john, mary = getPizzaPiece()
print(f"James{james}, Tohn {john}, Mary {mary}")

result = getPizzaPiece()
print("Pizza Result : ", result)
print(f"James{result[0]}, Tohn {result[1]}, Mary {result[2]}")

# type - unfixed inputs
def getAmount(*amt):
    result = 0
    for j in amt:
        result += j
    return result

today_sum = getAmount(100,200,348546,361,200)
print('오늘의 소득 :', format(today_sum,','))

# function(*arg,##karg) - 숙제 첫번째와 두번째가 떼거지로 들어올때

print()
cprint('Global,Local Variables')

# step1
gv = 10

def printV1(): # 다른 파일에 함수가 있어도 실행이 될까? 오류가 난다. 다른파일에서 gv가 존재해야만 한다.
    print('1-1단계 gv:',gv)

printV1()
print('1-2단계 gv:',gv)


# step2
def printV2():
    lv = 20
    print('2-1단계 gv:',gv)
    print('2-2단계 lv:',lv)
printV2()
print('2-3단계 gv:',gv)
# print('2-4단계 lv:',lv) # lv가 local 변수

# step 3
def printV3():
    # print('3-1단계 gv:',gv)
    gv = 30
    lv = 30
    print('3-2단계 gv:',gv)
    print('3-3단계 lv:',lv)

printV3()
print('3-4단계 gv:',gv)

# step 4
def printV4(gv):
    gv = 10
    print('4-1단계 gv:',gv)
    gv = 40
    print('4-2단계 gv:',gv)

printV4(gv)
print('4-3단계 gv:',gv)

# step 5
def printV5():
    lv = 50
    return lv

gv = printV5()
print('5-1단계 gv:',gv)

# step 6
gv1 = 61
gv2 = 62

def printV6():
    global gv1
    gv1 = 601
    globals()['gv2'] = 602
    gv2 = 702

printV6()
print('6-1단계 gv1:',gv1)
print('6-2단계 gv2:',gv2)
print(globals())

# step 7


if gv1 == 601: #local 문장으로 안봄
    local_new = 300

print('7-1단계 local_new :,', local_new)

i = 27632
for i in range(5): # local 문장으로 안봄
    print(i)

print('7-2단계 i:',i)




