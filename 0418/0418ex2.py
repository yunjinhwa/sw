'''
    2023.04.18
    윤진환
    문제분석
        변수
            num1, num2, total
        수식
            num1+num2
    #알고리즘
        1.변수선언
            num1, num2, total
        2.논리 (선택-중첩if)
            if num1>=75 and num2>=75 :
                if total>=180 :
                    '최우수 학생'
                elif 180>total>=160 :
                    '우수 학생'
                elif 160>total>=150 :
                    '보통 학생'
            elif num1<75 and num2<75 :
                '분발합시다'

'''

num1=int(input('첫번째 과목의 성적을 입력하시오'))
num2=int(input('두번째 과목의 성적을 입력하시오'))
total=num1+num2

if num1>=75 and num2>=75 :
    if total>=180 :
        print('최우수 학생')
    elif 180>total>=160 :
        print('우수 학생')
    elif 160>total>=150 :
        print('보통 학생')
elif num1<75 and num2<75 :
    print('분발합시다')


