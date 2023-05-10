'''
    2023.05.10
    윤진환
    별 출력
    문제분석
        변수-숫자(num)
    알고리즘
        1.변수 초기화
            num 정수입력
        2. 논리(중첩 반복)
            (반복) for i in range(1,num+1)
                (반복) for j in range(1,i+1)
                    별 찍기
'''

num1=int(input('숫자 입력'))

for i in range(1,num1+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

print('\n거꾸로 출력')

num2=int(input('숫자 입력'))

for i in range(num2,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print()

num3=int(input('숫자 입력'))

for i in range(1,num3+1):
    for j in range(i,num3+1):
        print('*',end='')
    print()



