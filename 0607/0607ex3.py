'''
    2023.06.07
    윤진환
    5명의 학생의 학번과 전화번호를 딕셔너리에 저장하고
    학번을 입력받아 해당 학생의 전화번호 출력하는 프로그램
    문제분석
        변수-phone, id, num
    알고리즘
        1.빈 딕셔너리 생성
        2.반복문(for)
            for i in range (5):
                id=학번저장
                num=전화번호 저장
        3.조건문(if)
            if id in phone: #학번이 전화번호부에 있는지 확인하는 문장
                맞는 전화번호 출력
'''

phone=dict()

for i in range(5):
    id=int(input(str(i+1)+"번째 학생 학번 입력: "))
    num=input("전화번호 입력: ")
    phone[id]=num
print("학생 전화번호부가 완성되었습니다.")

id=int(input("검색을 원하는 학생의 학번 입력: "))

if id in phone:
    print("입력한 학생의 전화번호: "+phone[id])
else:
    print("입력한 학생의 전화번호가 없습니다.")




