'''
    2023.04.11
    윤진환
    정수2개와 연산자 1개를 입력받아서 사칙연산 수행하는 프로그램
'''
num1=int(input('첫번째 숫자를 입력해 주세요'))
op=input('사칙연산자를 입력해 주세요')
num2=int(input('두번째 숫자를 입력해 주세요'))

if op == '+' :
    print(num1+num2)
elif op =='-' :
    print(num1-num2)
elif op =='*' :
    print(num1*num2)
elif op =='/' :
    print(num1/num2)



