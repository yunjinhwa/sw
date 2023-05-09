'''
    2023.05.09
    윤진환
    팩토리얼(!) 계산
    문제분석
        변수-num, ft
    알고리즘
        1.변수초기화
            num입력받기
            ft=1
        2.프로그램 논리(for)
            for i in range(num,0,-1)
'''

ft=1
num=int(input('팩토리얼 숫자 입력 : '))

for i in range(num,0,-1):
    ft=ft*i

print('%d의 팩토리얼 값은 : '%num,ft)

'''%d는 정수를 입력, %f는 실수'''




