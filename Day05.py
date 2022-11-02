from color import *
cprint('list')
weapon1 = ['도끼',1,3]
#우기의 이름을 꺼내오려면?
print(weapon1[0])
print()
weapons = [['도끼',1,3],['창',10,20],['검',15,17]]
my_weapons = weapons[1]
print(my_weapons)

cprint('color')
print(YELLOW +'노란색'+ END)
print(REDBG+'빨간바탕'+END)
print(GREENBG + BLACK + '녹색배경에 검정글자' + END)

for c in range(40, 48):
    print(f'\033[{c}m' + ' ' + END, end = '')
print()
for c in range(100, 108):
    print(f'\033[{c}m' + ' ' + END, end = '')
print()
for c in range(0, 256):
    print(f'\033[38;5;{c}m' + 'A' + END, end = '')
print()
for c in range(0, 256):
    print(f'\033[48;5;{c}m' + ' ' + END, end = '')
print()

#Homework
#총 256개의 배경색을 표현하되(True color)
#각 배경색의 r,g,b는 랜덤으로 결정한다.