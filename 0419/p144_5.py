'''
    2023.04.28
    윤진환
    #문제분석
        변수
            num1, num2
        수식
            num1//num2 == 0
    #알고리즘
        1. 변수선언
            num1, num2
        2. 논리 (if ~ else)
            if num1%num2 == 0 :
                print('{}는 {}의 약수입니다'.format(num2,num1))
            else :
                print('{}는 {}의 약수가 아닙니다.'.format(num2,num1))
'''

num1=int(input('첫번째 숫자를 입력해주세요'))
num2=int(input('두번째 숫자를 입력해주세요'))

if num1%num2 == 0 :
    print('{}는 {}의 약수입니다'.format(num2,num1))
else :
    print('{}는 {}의 약수가 아닙니다.'.format(num2,num1))


