'''
    2023.05.17
    윤진환
    파일 입출력
'''

with open("C:\data/Linetest.txt","r") as f: #파일 객체 생성(쓰기)
    for line in f: #파일 객체를 지정하여 반복문 작성

        print(line,end='') #end는 줄바꿈 안하기

#readline()
with open("C:\data/LineTest.txt","r") as f: #파일 객체 지정
    while True: #무한반복
        line=f.readline() #파일 한 줄씩 읽어오기
        print(line,end='') #줄바꿈 없이 출력

        if line=='': #무한반복 탈출조건
            break

#readlines()
with open("C:\data/LineTest.txt","r") as f:
    textLists = f.readlines()
    print(type(textLists))
    print(textLists)

#print()함수로 파일에 출력하기
f=open("C:\data/ptest.txt","w") #파일 객체 생성(쓰기)
print("aaaaaa",file=f) #파일 출력
print('bbbbbbb',file=f) #파일 출력
print("cccccc",file=f) #파일 출력
f.close() #파일 닫기