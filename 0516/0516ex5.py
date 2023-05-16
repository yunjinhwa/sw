'''
    2023.05.16
    윤진환
    read() 메소드 2번쨰
'''

ft = open("C:\data/test.txt","r") #파일 객체 생성(읽기)

print(ft.read(10),end='') #read로 읽은 10개의 문자 중 내용 첫번째 출력
print(ft.read(10),end='') #read로 읽은 10개의 문자 중 내용 두번째 출력
print(ft.read(10)) #read로 읽은 10개의 문자 중 내용 세번째 출력

ft.seek(0) #읽은 파일 처음으로 포인터 이동

print(ft.read(10),end='') #read로 읽은 10개의 문자 중 내용 첫번째 출력
print(ft.read(10),end='') #read로 읽은 10개의 문자 중 내용 두번째 출력
print(ft.read(10)) #read로 읽은 10개의 문자 중 내용 세번째 출력

ft.close()


