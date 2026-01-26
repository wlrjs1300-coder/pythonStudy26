# 회원관리에 관한 crud를 구현
# 부메뉴와 함께 run()메서드를 진행

class MemberService:
    def __init__(self):
        # 클래스 생성 시 필요한 변수들
        members = [] # 모든 회원이 들어있는 2차원 리스트
    def run(self):
        # 부메뉴 구현 메서드
        subrun = True
        while subrun:
            print("""
=====회원관리 메뉴=====
1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴
5. 로그아웃
9. 뒤로가기
            """)
            subSelect = input("선택 : ")
            if subSelect == "1":
                print("로그인 메뉴입니다")
            elif subSelect == "2":
                print("회원가입 메뉴입니다")
            elif subSelect == "3":
                print("회원수정 메뉴입니다")
            elif subSelect == "4":
                print("회원탈퇴 메뉴입니다")
            elif subSelect == "5":
                print("로그아웃 메뉴입니다")
            elif subSelect == "9":
                print("뒤로갑니다")
                subrun = False
            else:
                print("잘못된 번호를 입력하셨습니다")
                print("다시 입력하세요")