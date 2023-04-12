"""
    2023.04.12
    윤진환
    p145쪽 문제6번
"""

num1=int(input('첫번째 숫자를 입력하시오'))
num2=int(input('두번째 숫자를 입력하시오'))

if num1 % 2 == 0 and num2 % 2 ==0 :
    print('{}+{}={}'.format(num1,num2,num1+num2))
elif num1 % 2 == 1 and num2 % 2 ==0 :
    print('첫번째 정수를 짝수로 입력하세요')

elif num1 % 2 == 0 and num2 % 2 == 1 :
    print('두번째 정수를 짝수로 입력하세요')
else :
    print('두 숫자 모두 짝수로 입력하시오')




