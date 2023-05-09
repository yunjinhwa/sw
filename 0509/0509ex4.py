'''
    2023.05.09
    윤진환
    1~100까지의 입력받은 숫자의 배수만 더하기
    문제분석
        변수-i, total, num
    알고리즘
        1.변수초기화
            num은 정수입력받기
            i와 total은 초기화
        2. 프로그램 논리(while)
            while True:
                if i>100:
                    break
                if i%num==0:
                
                else :
                    
'''

i=1
total=0
num=int(input('합을 원하는 배수 입력'))

while True:
    if i>100:
        break
    if i%num==0:
        total=total+i
        i=i+1
        continue
    else :
        i=i+1
        continue

print(total)





