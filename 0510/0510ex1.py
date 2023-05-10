'''
    2023.05.10
    윤진환
    소수 검증 프로그램 만들기
    문제분석
        변수-숫자(num)
    알고리즘
        1. 변수 초기화
            num에 정수 입력
        2.논리(반복 안에 선택 포함)
            (반복) for i in range(2,num+1)
                (선택) if num%i==0
                       break
            (선택) if num==i:
                소수
            else :
                소수아님
'''

num=int(input('소수 검증 숫자 입력'))

for i in range(2,num+1):
    if num%i==0:
        break
if i==num:
    print('소수입니다.')
else :
    print('소수가 아닙니다.')
print('소수 판별 프로그램을 이용해주셔서 감사합니다.')






