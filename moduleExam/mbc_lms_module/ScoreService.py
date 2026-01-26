import os
class ScoreService:
    def __init__(self, file_name = "members.txt"):
        self.file_name = file_name
        self.members = []
        self.load_members()
    def load_members(self):
        self.members = []
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                self.members.append(data)
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}|{member[5]}|{member[6]}|{member[7]}\n")
    def score_add(self):
        print("성적 입력 메뉴입니다")
        sn = input("학번을 입력하세요 : ")
        for member in self.members:
            if member[0] == sn:
                print("이미 존재하는 학번입니다")
                return
        name = input("이름을 입력하세요 : ")
        kor = int(input("국어 점수를 입력하세요 : "))
        eng = int(input("영어 점수를 입력하세요 : "))
        mat = int(input("수학 점술를 입력하세요 : "))
        print(f"학번 : {sn} 이름 : {name} 국어 : {kor} 영어 : {eng} 수학 : {mat}")
        check = input("입력하신 정보가 맞으면 Y를 눌러주세요 : ").lower()
        if check == "y":
            tot = kor + eng + mat
            avg = tot // 3
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
            self.members.append([sn, name, kor, eng, mat, tot, avg, grade])
            print("입력완료")
            self.save_members()
            self.load_members()
            return
        else:
            print("다시 입력하세요")
    def score_list(self):
        print("성적 조회 메뉴입니다")
        sn = input("조회를 원하시는 학번을 입력하세요 : ")
        for member in self.members:
            if member[0] == sn:
                print(f"\n{member[1]}님의 성적")
                print(f"국어 : {member[2]} 영어 : {member[3]} 수학 : {member[4]} 총합 : {member[5]} 평균 : {member[6]} 학점 : {member[7]}\n")
                return
        print("찾을 수 없는 학번입니다")
    def score_modify(self):
        print("성적 수정 메뉴입니다")
        sn = input("수정을 원하시는 학번을 입력하세요 : ")
        found = False
        for member in self.members:
            if member[0] == sn:
                found = True
                self.score_modify_menu()
                select = input("선택 : ")
                if select == "1":
                    member[2] = int(input("변경 국어 점수 : "))
                elif select == "2":
                    member[3] = int(input("변경 영어 점수 : "))
                elif select == "3":
                    member[4] = int(input("변경 수학 점수 : "))
                else:
                    print("잘못된 번호를 입력했습니다")
                    return

                self.score_calculate(member)
                self.save_members()
                self.load_members()
                print("수정완료")
            if not found:
                print("잘못된 번호를 입력했습니다")
    def score_delete(self):
        print("성적 삭제 메뉴입니다")
        sn = input("삭제를 원하시는 학번을 입력하세요 : ")
        for idx, member in enumerate(self.members):
            if member[0] == sn:
                self.members.pop(idx)
                self.save_members()
                self.load_members()
                print("삭제완료")
    def score_modify_menu(self):
        print("""
=== 성적 수정 메뉴 ===
1. 국어 2. 영어 3. 수학
""")
    def score_calculate(self, member):
        kor = int(member[2])
        eng = int(member[3])
        mat = int(member[4])

        tot = kor + eng + mat
        avg = tot // 3

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

        member[5] = tot
        member[6] = avg
        member[7] = grade
    def run(self):
        subrun2 = True
        while subrun2:
            print("""
==== 성적관리 메뉴 ====
1. 성적 입력
2. 성적 조회
3. 성적 수정
4. 성적 삭제
5. 뒤로 가기
=====================
            """)

            subSelect2 = input("선택 : ")
            if subSelect2 == "1":
                print("성적입력 메뉴")
                self.score_add()
            elif subSelect2 == "2":
                print("성적보기 메뉴")
                self.score_list()
            elif subSelect2 == "3":
                print("성적수정 메뉴")
                self.score_modify()
            elif subSelect2 == "4":
                print("성적삭제 메뉴")
                self.score_delete()
            elif subSelect2 == "5":
                print("뒤로가기")
                subrun2 = False
            else:
                print("잘못된 번호를 입력했습니다")
                print("다시 입력하세요")