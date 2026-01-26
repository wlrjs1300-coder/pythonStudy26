from MemberPrac import MemberPrac

import os

class MemberServicePrac:
    def __init__(self, file_name = "members_prac.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_members()
    def load_members(self):
        self.members = []
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.members.append(MemberPrac.from_line(line))
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())

    def member_add(self):
        uid = input("아이디 : ")
        if self.find_member(uid):
            print("이미 존재하는 아이디")
            return
        pw = input("비밀번호 : ")
        name = input("이름 : ")

        self.members.append(MemberPrac(uid, pw, name))
        self.save_members()
        self.load_members()
        print("회원가입완료")


    def member_login(self):
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        member = self.find_member(uid)
        if not member:
            print("아이디 오류")
            return
        if not member.active:
            print("비활성화 아이디")
            return
        if member.pw == pw:
            self.session = member
            print("로그인 성공")
            if member.role == "admin":
                self.member_admin()
            else:
                self.member_modify()
        else:
            print("비밀번호 오류")

    def find_member(self, uid):
        for member in self.members:
            if member.id == uid:
                print(member.name, "님을 찾았습니다")
                return member
        return None
    def member_modify(self):
        subrun2 = True
        member = self.session
        while subrun2:
            print("\n[내정보메뉴]")
            print("1. 회원정보수정")
            print("2. 회원탈퇴")
            print("3. 로그아웃")
            print("9. 종료")

            sel = input("선택 : ")
            if sel == "1":
                print("\n[내정보수정]")
                print("1. 비밀번호")
                print("2. 이름")
                print("3. 계정 비활성화")
                print("4. 뒤로가기")
                sel2 = input("선택 : ")
                if sel2 == "1":
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경완료")
                elif sel2 == "2":
                    member.name = input("새 이름 : ")
                    self.save_members()
                    print("이름 변경 완료")
                elif sel2 == "3":
                    member.active = False
                    self.save_members()
                    print("계정 비활성화 완료")
                    self.session = None
                    return
                elif sel2 == "4":
                    continue

            elif sel == "2":
                delete = input("탈퇴하시려면 Y를 눌러주세요 : ").lower()
                if delete == "y":
                    self.members.remove(member)
                    self.save_members()
                    self.session = None
                    print("탈퇴완료")
                    return
            elif sel == "3":
                self.session = None
                print("로그아웃 완료")
                subrun2 = False
            elif sel == "9":
                break
    def member_admin(self):
        subrun = True
        while subrun:
            print("\n[관리자메뉴]")
            print("1. 회원리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("5. 로그아웃")
            print("9. 종료")

            sel = input("선택 : ")
            if sel == "1":
                self.member_list()
            elif sel == "2":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경완료")
            elif sel == "3":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    print("블랙리스트 처리완료")
            elif sel == "4":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin / manager / user : ").lower()
                    self.save_members()
                    print("권한 변경완료")
            elif sel == "5":
                self.session = None
                print("로그아웃 완료")
                subrun = False
            elif sel == "9":
                break

    def member_list(self):
        print("\n[회원목록]")
        print("*"*60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태'}")
        print("*" * 60)
        for member in self.members:
            status = "활성화" if member.active else "비활성화"
            print(f"{member.id:10} {member.name:10} {member.role:10} {status:10}")
        print("*" * 60)

    def main_menu(self):
        print("""
=== 회원관리 프로그램 ===
1. 로그인 2. 회원가입 3. 종료
        """)
    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input("선택 : ")
            if sel == "1":
                print("\n[로그인]")
                self.member_login()
            elif sel == "2":
                print("\n[회원가입]")
                self.member_add()

            elif sel == "3":
                print("\n[종료]")
                run = False
            else:
                print("잘못된 번호 입력")