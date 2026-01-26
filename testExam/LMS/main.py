from testExam.LMS.common.Session import *
from testExam.LMS.service import *

def main():
    MemberService.load()
    run = True
    while run:
        print("""
======== MBC 아카데미 회원관리 프로그램 ========
1. 로그인     2. 회원가입     3. 회원정보 수정
4. 관리자 메뉴 5. 회원탈퇴 6. 로그아웃 9. 종료
============================================
        """)
        member = Session.login_member
        if member is None:
            print("현재 로그인 상태가 아닙니다")
        else:
            print(f"{member.name}님 환영합니다")
        sel = input("선택 : ")
        if sel == "1": MemberService.login()
        elif sel == "2": MemberService.signup()
        elif sel == "3": MemberService.modify()
        elif sel == "4": MemberService.admin_menu()
        elif sel == "5": MemberService.delete()
        elif sel == "6": MemberService.logout()
        elif sel == "9":
            print("프로그램 종료")
            run = False
if __name__ == "__main__":
    main()