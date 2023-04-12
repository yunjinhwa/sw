'''
    2023.04.12
    윤진환
    실습예제 4-5

    문제분석
        변수-평점(jumsu)
    알고리즘
        1.변수선언
            jumsu에 평점 실수로 입력받기
        2.조건충족여부 확인
            if jumsu >= 4.2 :
        3.결과 출력
'''

jumsu=float(input('Enter your score')) #float는 입력받은 문자열을 실수로 변환

if jumsu >= 4.2 :
    print('당신의 평점은 : {}'.format(jumsu))
    print('해외 연수 기회 부여')
else :
    print('당신의 평점은 : {}'.format(jumsu))



