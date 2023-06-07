'''
    2023.06.07
    윤진환
    랜덤으로 난수 생성하여 10개짜리 세트 두개를 만들어서 교,차,합집합 구하기
    문제분석
        변수-num1, num2
    알고리즘
        1.랜덤 모듈 추가
        2.비어있는 세트 2개 생성
        3.반복문
            while True:
                if len(num1)==10 and len(num2==10):
                    break
                세트요소 추가
        4.합집합, 교집합, 차집합
'''

import random

num1=set() #딕셔너리도 중괄호를 사용하므로 set함수를 사용하여 빈 세트 생성
num2=set()

while True:
    num1.add(random.randint(1,100))
    num2.add(random.randint(1,100))
    if len(num1)==10 and len(num2)==10:
        break

print("발생된 10개의 난수 num1 : ",num1)
print("발생된 10개의 난수 num2 : ",num2)

print("num1, num2의 합세트",num1|num2)
print("num1, num2의 교세트",num1&num2)
print("num1, num2의 차세트",num1-num2)

