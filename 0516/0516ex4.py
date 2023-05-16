'''
    2023.05.16
    윤진환
    파일 입출력 (읽기)
'''

f = open("C:\data/test.txt","r")

print(f.read(10))
print(f.read(10))
print(f.read(10)) #포인터는 이미 네번째 줄에 있음 즉 print는자동으로 줄바꿈 되므로 한줄이 띄워져서 출력된다

f.close()