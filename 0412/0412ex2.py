'''
    2023.04.12
    윤진환
    실습예제 4-8

    문제분석
        변수-숫자1(num1), 숫자2(num2)
    알고리즘
        1.변수선언
            num1,num2에 정수 입력
        2.조건 충족 여부 확인
            if num1 > num2 :
'''

num1=int(input('첫번째 숫자 입력')) #첫번째 변수 입력받기
num2=int(input('두번째 숫자 입력')) #두번째 변수 입력받기

if num1 > num2 : #조건
    print('두 수중에 큰수는 {}이고, 작은수는 {}입니다.'.format(num1,num2)) #조건이 참일 경우 출력
else :
    print('두 수중에 큰수는 {}이고, 작은수는 {}입니다.'.format(num2,num1)) #조건이 거짓일 경우 출력




