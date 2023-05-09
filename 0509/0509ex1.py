'''
    2023.05.09
    윤진환
    두 개의 숫자를 입력 받아서 두 수 사이의 합계 구하기
    문제분석
        변수-num1, num2, temp, sum, i
    알고리즘
        1.변수선언
            num은 입력받기
            sum=0, temp=0
        2.프로그램 논리(선택,반복)
            2-1(선택조건) - 항상 num1<=num2
                if num1>num2
                    num1과 num2의 값을 바꾼다
            2-2(반복조건) - num1~num2까지 1씩 증가하면서 더하기
                while i>=num2
                    sum=sum+i
                    i=i+1                
'''

temp=0
sum=0
num1=int(input('첫번째 숫자를 입력하시오'))
num2=int(input('두번째 숫자를 입력하시오'))

if num1>num2: #선택조건
    temp=num1 #num1값을 temp에 저장
    num1=num2 #num2값을 num1에 저장
    num2=temp #temp값을 num2에 저장

i=num1 #i초기화
while i<=num2: #반복조건
    sum=sum+i #합계 구하기
    i=i+1 #i 1씩 증가

print('{}~{}까지의 합계는 {}'.format(num1,num2,sum))
    






