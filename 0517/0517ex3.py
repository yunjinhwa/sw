'''
    2023.05.17
    윤진환
    학생 이름 성적 저장 프로그램
    문제분석
        변수-학생이름과 성적(info)
    알고리즘
        1.파일 객체 생성(쓰기)
        2.반복문
            while i<=5:
                info = input이름성적
                파일로 출력
        3.파일종료
'''

f=open("C:\data/stu.txt","w") #파일 객체 생성(쓰기)

i=1
while i<=5: #반복 조건
    info = input("%d번째 학생 이름과 3과목 성적 입력(예: 홍길동 80 90 70) : "%i) #이름 성적 입력
    f.write(info+"\n") #파일에 저장
    i+=1
f.close() 