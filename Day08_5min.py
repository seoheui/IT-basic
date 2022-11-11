"""
    String Comparison
    2022.11.11
"""
"""
    0.타이틀 출력
    1.문자열을 2개 입력받는다.
    2.공통으로 존재하는 문자를 찾는다.(set.intersection 이용)
    3."첫번째 문자열의 길이:*,두번째 문자열의 길이: *"
      "공통으로 존재하는 문자개수:*"을 출력
    4. 첫번째 문자열과 두번째 문자열을 출력하되 공통된 문자를 각각 빨간색으로, 초록색으로 색을 입혀 출력한다.
"""
from color import *
cprint("String Comparison")

str1 = input("첫번째 문자열을 입력하세요:")
str2 = input("두번째 문자열을 입력하세요:")
set1 = set(str1)
set2 = set(str2)
intersection = set1.intersection(set2)
if ' ' in intersection:
    intersection.remove(' ')
list_intersection = list(intersection)#필요없음
print(intersection)
print("첫번째 분자열의 길이 :", len(str1))
print("두번재 문자열의 길이 :", len(str2))
print("공통으로 존재하는 문자 개수 :", len(list_intersection))
for s in str1:
    if s in intersection:
        print()





cprint("String Comparator")
str1 = input('첫 번쩨 문자열 입력 :')
atr2 = input('두 번째 문자열 입력 :')

#고생하는 방법
str1_list = []
str2_list = []
for c in str1:
    str1_list.append(c)
for c in str2:
    str2_list.append(c)

set1 = set(str1_list)
set2 = set(str2_list)

# 도련님 방식
set1 = set(str1)
set2 = set(str2)

common = set1.intersection(set2)
if ' ' in common:
    common.remove(' ')
print(common)

print(f"첫번째 문자열의 길이: {len(str1)}, 두번째 문자열의 길이 {len(str2)}")
print(f"공통으로 존제하는 문자 개수 :{len(common)}")

for c in str1:
    if c in common:
        print(BLUE + c + END, end ='')
    else:
        print(c, end='')
print()
for c in str2:
    if c in common:
        print(BLUE + c + END, end ='')
    else:
        print(c, end='')


# 추가과제
# 공통으로 존재하는 단어 찾기(스페이스, 쉼표,마침표로 구분이 되어있음)









