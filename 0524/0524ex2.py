'''
    2023.05.24
    윤진환
    문제정의
        score1.txt파일을 읽어와서 각 학생의 등급을 결정하고
        결과를 report1.txt파일에 저장하기
'''

score=[] #리스트 변수 생성

f=open("C:\data/score1.txt","r")

for i in range(10):
    score.append(f.readline().split()) #한 줄씩 읽어서 공백을 기준으로 나누고 score리스트에 추가

for j in range(10):
    score[j][1]=float(score[j][1]) #문자열 실수로 변환

    if score[j][1]>=90:
        score[j].append("A")
    elif score[j][1]>=80:
        score[j].append("B")
    elif score[j][1]>=70:
        score[j].append("C")
    elif score[j][1]>=60:
        score[j].append("D")

for i in range(10):
    print("{:<5}{:>5}".format(score[i][0],score[i][1]))


f.close()


