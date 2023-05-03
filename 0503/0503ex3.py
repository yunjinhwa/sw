'''
    2023.05.03
    윤진한
    1~입력받은 숫자까지의 합계 구하기
    문제분석
        변수-sum, num
    알고리즘
        변수선언
            sum지정, num입력받기
        반복문(for)
            for i in range(1,입력받은 숫자+1)
                sum=sum+i
            출력
        변수선언
            sum,i지정, num입력받기
        반복문(while)
            while i<=num
                sum=sum+i
                i=i+1
            출력
'''

#for 반목문
sum=0
num=int(input('숫자를 입력하시오'))
for i in range(1,num+1) :
    sum=sum+i
print(sum)

#while 반복문
i=1
sum=0
num=int(input('숫자를 입력하시오'))
while i<=num :
    sum=sum+i
    i=i+1
print(sum)




