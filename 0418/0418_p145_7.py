'''
    2023.04.18
    윤진환
    #문제분석
        변수:X,Y
        수식:X+Y, X*Y, X//Y
    #알고리즘 
        1.변수선언
            X,Y
        2.논리 (if)
            if X>Y :
                if Y==0 :
                    print('Y의 값이 0입니다. 다른 수를 입력해주세요')
                else :
                        print(X//Y)
            elif X<Y :
                print(X+Y)
            elif X==Y :
                print(X*Y)
            
'''

X=int(input('첫번째 숫자를 입력하세요'))
Y=int(input('두번째 숫자를 입력하세요'))

if X>Y :
    if Y==0 :
        print('Y의 값이 0입니다. 다른 수를 입력해주세요')
    else :
            print(X//Y)
elif X<Y :
    print(X+Y)
elif X==Y :
    print(X*Y)



