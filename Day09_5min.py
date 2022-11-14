"""
1. 함수를 design
2. 외부로부터 str을 받는다.
3. str이 숫자와 -로만 구성되어 있는지 check
4. 3이 통과라면 총 10자리 또는 11자리 숫자인지 check
5. 정상이면 10자리면 XXX, XXX, XXXX, return
         11자리면 XXX,XXXX,XXXX,를 return
    cf)정규표현식(regular expression) : 0-9,A-Za-z, 가-힣
"""
def PhoneNumber(strs):
    if '-' in strs:
        Flag = True
        list = []
        while Flag:
            for i in range (10):
                str_i = str(i)
                if str_i in strs:
                    if len(strs) == 12:
                        list = strs.split('-')
                    elif len(strs) == 13:
                        list = strs.split('-')
                else:
                    continue
                return list[0], list[1], list[2]
            Flag = False
print(PhoneNumber('010-3620-4229'))
print(PhoneNumber)