'''
    2023.05.03
    윤진환
    구구단 전체 출력
    문제분석
        변수-i,j
    알고리즘
        논리(반복-중첩 반복(for))
        (조건) for i in range(2,10)
            제목출력
                for j in range(1,10)
                    구구단 출력
'''

for i in range(2,10) :
    print('-----',i,'단-----')
    for j in range(1,10) :
        print('{}X{}={}'.format(i,j,i*j))







