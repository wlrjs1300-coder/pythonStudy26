# Member 객체를 crud 기능 넣기
# 메뉴 구현
# 텍스트 파일화 (파일 읽기, 파일 저장)
# 회원 가입, 로그인, 로그아웃, 회원수정, 회원탈퇴
from Member import Member # 회원 객체 추가 연결
# 사용법 : member = Member() -> 객체 생성
#         member.필드or메서드
import os
class MemberService:
    def __init__(self, file_name = "members.txt"):
        # 클래스가 생성할 때 초기값 관리
        self.file_name = file_name
        self.members = [] # 회원들을 리스트로 만들어 Member() 객체를 담음
        self.session = None # 로그인 상태를 담당(members의 인덱스 보관용)
        self.load_members() # 아래 쪽 메서드 호출

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input("선택 : ")
            if sel == "1":
                self.member_add()
            elif sel == "2":
                self.member_login()
            elif sel == "3":
                self.member_logout()
            elif sel == "4":
                self.member_modify()
            elif sel == "5":
                self.member_delete()
            elif sel == "9":
                run = False
            else:
                print("잘못 입력했습니다")

    def load_members(self): # 파일에서 메모리로 불러옴
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = [] # 메모리에 남은 값을 초기화
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))
                #                   Member객체 .from_line() 메세드 실행
                #                              1줄을 가져와 클래스로 만듬
                #   members 리스트 뒷부분에 추가

    def main_menu(self):
        print("""
=== 회원관리 프로그램 (Member 객체 기반) ===
1. 회원가입 2. 로그인 3. 로그아웃
4. 회원정보 수정 5. 회원탈퇴 9. 종료
        """)

    def member_add(self):
        print("\n[회원가입]")
        uid = input("ID : ")

        if self.find_member(uid): # 자주쓰는 중복코드로 메서드 처리
            print("이미 존재하는 아이디")
            return
        pw = input("Password : ")
        name = input("Name : ")
        role = "user" # 없어도됨

        self.members.append(Member(uid, pw, name, role))
        #                   Member클래스의 init메서드로 바로 들어가 객체 생성
        self.save_members()
        self.load_members()
        print("화원가입완료")

    def member_login(self):
        print("\n[로그인]")
        uid = input("ID : ")
        pw = input("Password : ")
        
        member = self.find_member(uid)
        
        if not member:
            print("아이디 오류")
            return
        if not member.active:
            print("비활성화 아이디")
            return
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인 성공 ({member.role})")
            
            if member.role == "admin":
                self.member_admin() # 관리자용 메서드
        else:
            print("비밀번호 오류")

    def member_logout(self):
        pass

    def member_modify(self):
        pass

    def member_delete(self):
        pass

    #파일 저장용 코드
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())
                #       Member 객체의 메서드를 사용하여 1줄 씩 기록

    # id를 이용해 members를 찾는 공동 메서드
    def find_member(self, uid):
        for member in self.members:
        # members 리스트에서 1개씩 member객체를 가져와
            if member.id == uid: # 가져온 member 객체.id와 전달받은 id가 같은지
                print(member.name, "님을 찾았습니다")
                # 예전에는 member[]으로 찾았는데 지금은 변수명으로 찾을 수 있음
                return member # 같은게 있으면 member객체로 리턴
        return None # 없으면 None으로 리턴

    def member_admin(self):
        # role = "admin" 에 진입한 메서드
        subrun = True
        while subrun:
            print("\n[관리자메뉴]")
            print("1. 회원리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")

            # 회원 목록 보기
            sel = input("선택 : ")
            if sel == "1":
                self.show_member_list()
            # 비밀번호 변경
            elif sel == "2":
                uid = input("대상 ID : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("New Password : ")
                    self.save_members()
                    print("비밀번호 변경 완료")
                else:
                    print("회원 없음")
            elif sel == "3":
                uid = input("ID : ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    print("블랙리스트 처리 완료")
                else:
                    print("회원 없음")
            elif sel == "4":
                uid = input("ID : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin / manager / user : ")
                    self.save_members()
                    print("권한 변경 완료")
                else:
                    print("회원 없음")
            elif sel == "9":
                subrun = False
            else:
                print("잘못된 번호를 입력하였습니다")
                print("다시 입력하세요")

    def show_member_list(self):
        # 관리자가 볼 수 있는 회원 리스트들
        print("\n[회원 목록]")
        print("-"*60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")
        print("-"*60)

        for member in self.members:
        # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성화" if member.active else "비활성화"
            # member.active 가 True면 status 변수에 "활성화", False라면 "비활성화"
            print(f"{member.id:10} {member.name:10} {member.role:10} {status}")
            #                                                        "활성화"or"비활성화"
        print("-"*60)