'''
    2023.04.05
    윤진환
    수령액 구하기
'''
get=0
born=0
sweetwater=0
fuck=0
max=0

born=int(input('본봉을 입력하시오')) #본봉 입력
sweetwater=int(input('수당을 입력하시오')) #수당 입력

max=born+sweetwater #총액 계산
fuck=max/5 #세금 계산
get=max-fuck #수령액 계산

print('수령액은 {}원 입니다.'.format(get))

