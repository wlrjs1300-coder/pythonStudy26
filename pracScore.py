menu = """
==========================
MBC 아카데미 성적관리 프로그램
==========================
1. 성적 등록
2. 성적 조회
3. 성적 수정
4. 성적 삭제
5. 프로그램 종료
"""

sns = []
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grades = []

run = True
login_user = None

while run:
    print(menu)
    select = input("원하는 메뉴를 골라주세요 : ")
    if select == "1":
        print("성적 등록 메뉴를 선택하였습니다")
        sn = input("학번을 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        kor = input("국어 점수 : ")
        eng = input("영어 점수 : ")
        mat = input("수학 점수 : ")
        print("학번 : "+sn)
        print("이름 : "+name)
        print("국어 점수 : "+kor)
        print("영어 점수 : "+eng)
        print("수학 점수 : "+mat)
        print("입력하신 정보가 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ") == "y":
            kor = int(kor)
            eng = int(eng)
            mat = int(mat)
            tot = kor+eng+mat
            avg = tot/3
            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            elif avg >= 60:
                grade = "D"
            else:
                grade = "F"
            kors.append(kor)
            engs.append(eng)
            mats.append(mat)
            tots.append(tot)
            avgs.append(avg)
            grades.append(grade)
            print("\n성적 등록 완료")
            print(f"학번: {sn} | 이름: {name}")
            print(f"국어: {kor} | 영어: {eng} | 수학: {mat}")
            print(f"총합: {tot} | 평균: {avg} | 학점: {grade}")
    elif select == "2":
        print("성적 조회 메뉴를 선택하였습니다")
    elif select == "3":
        print("성적 수정 메뉴를 선택하였습니다")
    elif select == "4":
        print("성적 삭제 메뉴를 선택하였습니다")
    elif select == "5":
        print("프로그램 종료 메뉴를 선택하였습니다")
    else:
        print("1~5번 메뉴에서 골라주세요")