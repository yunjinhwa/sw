'''
    2023.05.23
    윤진환
    문제정의
        stu.txt파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
    문제분석
        변수-한줄씩 읽어서 저장(score), 리스트 자료로 변환하기 위해(scorelist)
            리스트에서 이름 항목 저장(name) 합계(sum)
    알고리즘
        1.파일 객체 생성(쓰기)
        2.파일 처리
            2-1 (반복)while True:
                        한줄 읽어서 score에 저장 
                        (선택) if score=='':
                                break
                        읽어온 내용을 리스트로 변환해서 scorellist 저장
                        scorelist에서 첫번째 항목(이름)을 name변수에 저장
                        (반복) for i in range(1,4):
                                scorelist의 1,2,3 항목의 값을 sum에 더하기
'''

f=open("C:\data/stu.txt",'r') #읽기모드 파일 객체 생성
while True: #무한반복
    score=f.readline() #한 줄씩 읽어 오기

    if score=='': #더이상 읽어 올 내용이 없다면
        break #반복 종료

    scorelist=score.split()

    name=scorelist[0] #리스트 첫번쨰 항목은 이름

    sum=0 #합계

    for i in range(1,4):
        sum=sum+int(scorelist[i]) #3과목 성적의 합계

    print(name+"의 평균성적은 : %.1f"%(sum/3)) #% 쓸 떄는 변수 만들지 않고 간단한 수식은 괄호안에 넣으면 된다.

f.close() #파일 닫기