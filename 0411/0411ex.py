'''
    2023.04.11
    윤진환
    선택문 (if, if else)
    (1)입력받은 성적이 80이상이면 '합격' 출력
        그리고 성적과 상관없이 '수고했습니다.' 출력
    (2)성적이 80이상이면 '합격' 출력
        성적이 80미만이면 '불합격' 출력
        성적과 관계 없이 '수고하셨습니다.' 출력
        
'''

#단순 if문
score=int(input('점수를 입력해주세요')) #점수 정수로 입력

if score>=80 : #선택 조건
    print('합격') #참 일때만 실행

print('수고하셨습니다.') #if문 상관없이 출력

#이중 if

jumsu=int(input('점수를 입력해주세요')) #정수 입력

if jumsu>=80 : #선택조건
    print('합격') #조건이 참 일때만 실행
else :
    print('불합격') #조건이 거짓 일때만 실행
print('수고하셨습니다') #if else문 상관없이 실행


