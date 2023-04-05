'''
    2023.04.05
    윤진환
    5과목 점수 입력 받아서 합계 평균 구하기(p117-14)
'''

sub1=0
sub2=0
sub3=0
sub4=0
sub5=0
total=0
avg=0

sub1=int(input('첫번째 과목 점수 입력:'))
sub2=int(input('두번째 과목 점수 입력:'))
sub3=int(input('세번째 과목 점수 입력:'))
sub4=int(input('네번째 과목 점수 입력:'))
sub5=int(input('다섯번째 과목 점수 입력:'))

total=sub1+sub2+sub3+sub4+sub5
avg=total/5

print('과목총점은 {}점, 과목평균은 {}점 입니다.'.format(total,avg))


