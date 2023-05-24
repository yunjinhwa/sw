'''
    2023.05.24
    윤진환
    문제정의
        난수를 발생시켜 5개짜리 줄 5개 만들어서 파일을 생성하고 생성한 파일을 읽어 각 학생의 평균 구하기
    문제분석
        변수-
'''

import random #난수 모듈 추가

with open("C:\data/num.txt","w") as f: #파일 객체
    for i in range (5): #줄반복
        for j in range(5): #랜덤 수 찍기 반복
            f.write(str(random.randint(1,100))) #랜덤 수 파일에 쓰기
            f.write(' ') #숫자 다음 공백 찍기
        f.write('\n')

with open("C:\data/num.txt","r") as f1 :
    with open("C:\data/avg.txt", "w") as f2 :

        j=0
        while True:
            j=j+1
            score=f1.readline() #num파일에서 한줄 읽어오기
            if score=='':
                break
            scorelist=score.split() #읽어 온 한줄을 공백 기준 리스트로
            
            sum=0
            for h in range(5):
                sum=sum+int(scorelist[h]) #리스트의 항목 더하기
            print(j,"번 학생의 평균",sum/5,file=f2) #결과 파일에 작성

