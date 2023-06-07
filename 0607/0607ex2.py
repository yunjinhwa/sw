'''
    2023.06.07
    윤진환
    로또번호 생성하기
    문제분석
        변수-lotto, i
    알고리즘
        1.랜덤 모듈 추가
        2.빈 세트 생성
        3.반복문(무한반복)
            while True:
                if len(lotto)==6:
                    break
'''

import random

lotto=set()
i=0

while True:
    if len(lotto)==100000:
        break
    lotto.add(random.randint(1,100000))

    i=i+1

print("이번주 로또 넘버: ",sorted(lotto))
print("중복된 난수의 발생 횟수: ",i-100000)



