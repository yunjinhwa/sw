'''
    2023.05.10
    윤진환
    
    문제분석
        변수-합계(total), 입력횟수(count), 평균(avg), 숫자(num)
    알고리즘
        1. 변수 초기화
            avg, count, total=0
        2.논리 (반복안에 선택 포함)
            (반복)while True:
                num 입력받기
                total 더하기
                count 1증가
        3.합계, 평균 출력
'''

total=0; count=0; avg=0

while True:
    if total>=1000:
        break
    num=int(input('숫자 입력'))
    total += num
    count += 1#count 1증가
avg=total/count
print('1000을 넘은 수 : %d'%total)
print('평균은 : %.2f' %avg)





