'''
    2023.05.16
    윤진환
    파일 입출력 - 읽기(read()-전체 내용을 하나의 문자열로 반환)
'''

ft = open("C:\data/test.txt","r") #파일 객체 생성(읽기)

txts = ft.read() #변수 선언(read로 읽은 내용을 변수로 지정)

print(txts) #출력

ft.close()

