from color import *

cprint('Method of List')
list_a = [1,2,3]
print(list_a)
# list_a[3] = 4 # IndexError
list_a.append(4)
print(list_a)
list_a.append('abcde')
print(list_a)
list_a.append([100,200,300])
print(list_a)
list_a.insert(6, 65555)
print(list_a)
list_a.insert(10000,200) # 범위 벗어나면 맨 뒤에 붙임
print(list_a)

a = [4,5,6]
b = (444,555)
c = {123,456,789}
list_a.extend(a)
list_a.extend(b)
list_a.extend(c)
print(list_a)
list_a.insert(16, a)
print(list_a)

print()
print('pop,remove,index')
basket = list_a.pop()
print(list_a)
dish = list_a.pop(0)
print(list_a)

g = list_a.index(444)
print(f'444는 {g}위치에 있음')
# g2 = list_a.index(444,11,15) #못찾으면 오류(ValueError)

# 미리보는 해결책
try :
    g2 = list_a.index(444, 11, 15)
except ValueError:
    print('데이터 없던데')
    print('그러나 정상 종료')

list_a.remove(555) # 값이 없으면 ValueError
print(list_a)

list_a.clear()
print(list_a)

cprint("Set Method")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a.intersection(b)
d = a.union(b)
e = a.difference(b)
print(c,d,e,sep='|')

s1 = "Biden appears to avoid the midterm Democratic purge many in his party feared"
s2 = "Herschel Walker and Raphael Warnock locked in too-early-to-call Georgia Senate race"
#s1과 s2에 동시에 존재하는 글자 찾기
list_s1 = []
list_s2 = []
for s in s1:
    list_s1.append(s)
list_s1= set(list_s1)
print(list_s1)
for s in s2:
    list_s2.append(s)
list_s2 = set(list_s2)
print(list_s2)
a = list_s1.intersection(list_s2)
print(a)
#'와, 공백은 제외하시오.

set_s1 = set(s1)
set_s2 = set(s2)
result = (set_s1.intersection(set_s2))
result = list(result)
if "'" in result:
    result.remove("'")
if "," in result:
    result.remove(",")
if " " in result:
    result.remove(" ")

print(result)
cprint("Dictionary Method")
dic = {1:'one', 'subject':['science','korean'],'숫자':1234}
print(dic[1])
print(dic.get(1))
print(dic.get(8,'Not exists'))
print(list(dic.keys()))
dic[8]=500
print(list(dic.keys()))


