'''
    2023.05.09
    윤진환
    1~1000까지의 입력받은 숫자의 배수만 더하기
    문제분석
        변수-num, total
    알고리즘
        1.변수 초기화
            num에 정수 입력
            total=0
        2.프로그램 논리(반복for)
            for i in range(num,1001,num):
            sum=sum+1
'''

total=0
num=int(input('합을 원하는 배수 입력'))

for i in range(num,1001,num):
    total=total+i
print(total)







