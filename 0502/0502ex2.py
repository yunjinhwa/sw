'''
    2023.05.02
    윤진환
    range()함수 순차적 범위의 숫자 생성하는 함수
'''

for i in range(10) : #반복 조건
    print(i) #반복 조건이 참일 동안 반복
'''
    i에는 range()가 만들어 내는 숫자가 차례대로 들어간다
    위의 두 문장은 0부터 9까지 출력해낸다
    print는 줄바꿈되므로 세로로 출력된다.
'''

for i in range(10) : #반복 조건
    print(i,end=' ') #반복 조건이 참일 동안 반복
'''
    i에는 range()가 만들어 내는 숫자가 차례대로 들어간다
    위의 두 문장은 0부터 9까지 출력해낸다
    end=' '로 인해 가로로 출력된다.
'''

print()

for i in range(10) : #반복 조건
    print(i) #반복 조건이 참일 동안 반복

print()

for i in range(10) : #반복 조건
    print(i,end=' ') #반복 조건이 참일 동안 반복

print()

for j in range(1,11,2) : #반복조건
    print(j,end=' ') #홀수 출력

print()

for num in range(10,0,-1) : #반복 조건
    print(num,end=' ') #역순 출력





