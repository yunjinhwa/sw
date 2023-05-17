'''
    2023.05.17
    윤진환
    파일 복사 프로그램
    문제분석
        변수-source, target, txt
    알고리즘
        1.변수선언(복사할 파일주소,붙혀넣을 파일주소)
        2.복사 할 파일열기
        3.파일내용 읽고 변수에 저장
        4.붙혀넣기 할 파일 열기
        5.붙혀넣기
        6.결과출력
'''

source=input("source 파일 입력 : ") #source 파일주소 입력받기
target=input("target 파일 입력 : ") #target 파일주소 입력받기

with open(source,"r") as f: #source 파일 객체 생성(읽기)
    txts=f.read() #파일 읽고 txts변수에 저장
with open(target,"w") as f: #target 파일 객체 생성(쓰기)
    f.write(txts) #txts변수의 내용 파일로 출력

print(target+"파일이 생성되었습니다.") #결과 출력

