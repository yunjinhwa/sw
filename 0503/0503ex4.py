'''
    2023.05.03
    윤진환
    문제정의
    입력받은 구구단 출력하기
    문제분석
        변수-단(dan), 반복횟수(i)
    알고리즘
        1.변수선언
            dan은 정수로 입력
            i=1
        2.반복문(while)
            while i<=9 :
                구구단 출력
'''

dan=int(input('단 입력'))
i=1
print('-----',dan,'단 -----')
while i<=9 :
    print('{}X{}={}'.format(dan,i,dan*i))
    i=i+1




