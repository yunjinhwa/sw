'''
    2023.04.04
    윤진환
    표준출력(print) format()연습
'''
print('이름은 {}이고 나이는 {}살 입니다'.format('윤진환',19))
print('이름 : {name}, 나이 : {age}, 주소 : {add}'.format(add='경남 김해시 율하3로 100 716동 2104호',age=19,name='윤진환'))
print('The lucky number is ({:14})'.format(7777))
print('The lucky number is ({:<14})'.format(7777)) # :는 글자는 왼쪽 숫자는 오른쪽 정렬, :<는 왼쪽정렬, :>오른쪽 정력, :^가운데 정렬
name = input('이름입력 : ') #input을 사용해 키보드로 입력받은 값은 문자열로 변환됨 즉 변수를 산술계산 할 수 없음
int(input('국어 성적 입력 : ')) #정수로 입력받고 싶을 때는 int안에 input 사용



