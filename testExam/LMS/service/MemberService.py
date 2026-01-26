import os
from testExam.LMS.common.Session import *
from testExam.LMS.domain import Member

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"..","data","member.txt")

class MemberService:
    members = []
    @classmethod
    def load(cls):
        if not os.path.exists(FILE_PATH):
            cls.save()
            return
        with open(FILE_PATH,"r",encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))
    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line()+"\n")
    @classmethod
    def login(cls):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화 아이디입니다")
                    return
                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.name}님 로그인 성공 ({m.role})")
                    print(m)
                    return
                else:
                    print("비밀번호가 일치하지 않습니다")
                    return
        print("아이디를 찾을 수 없습니다")
    @classmethod
    def logout(cls):
        Session.logout()
        print("로그아웃 완료")
    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                print("이미 존재하는 아이디입니다")
                return
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        member = Member(uid,pw,name)
        cls.members.append(member)
        cls.save()
        print("회원가입 완료")
    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        member = Session.login_member
        print("""
[내 정보 수정]
1. 이름 수정
2. 비밀번호 수정
0. 뒤로가기
        """)
        sel = input("선택 : ")
        if sel == "1":
            member.name = input("새 이름 : ")
            print(f"회원님의 이름이 ({member.name})로 변경되었습니다")
        elif sel == "2":
            member.pw = input("새 비밀번호 : ")
            print(f"회원님의 비밀번호가 ({member.pw})로 변경되었습니다")
        elif sel == "0":
            return
        cls.save()
        print("정보 수정 완료")
    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        member = Session.login_member
        print("""
[회원 탈퇴]
1. 영구 탈퇴
2. 계정 비활성화
0. 뒤로가기
        """)
        sel = input("선택 : ")
        if sel == "1":
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("영구 탈퇴 완료")
        elif sel == "2":
            member.active = False
            Session.logout()
            cls.save()
            print("계정 비활성화 완료")
        elif sel == "0":
            return
    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자 전용 메뉴입니다")
            return
        while True:
            print("""
[관리자 전용 메뉴]
1. 회원리스트 조회
2. 회원 권한 수정
3. 블랙리스트 관리
0. 뒤로가기
            """)
            sel = input("선택 : ")
            if sel == "1":
                cls.list_member()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel == "0":
                break
    @classmethod
    def list_member(cls):
        print("\n[회원리스트 조회]")
        for m in cls.members:
            print(m)
    @classmethod
    def change_role(cls):
        print("\n[회원 권한 수정]")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.role = input("admin / manager / user : ").lower()
                cls.save()
                print("권한 수정 완료")
                return
        print("회원 없음")
    @classmethod
    def block_member(cls):
        print("\n[블랙리스트 관리]")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("블랙리스트 처리 완료")
                return