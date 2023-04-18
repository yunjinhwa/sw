'''
    2023.04.18
    윤진환
    성적처리 프로그램(중첩if문)
    성적이 90이상이면 'A', 90미만 80이상이면 'B',
    80미만 70이상이면 'C', 70미만이면 'F' 출력
'''

num1=int(input('성적을 입력하시오'))

if num1>=70:
    if num1>=80:
        if num1>=90:
            print('A')
        else :
            print('B')
    else :
        print('C')
else :
    print('F')



