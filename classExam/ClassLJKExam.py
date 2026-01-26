import os

class MemberManager: # 객체를 담당하는 클래스 사용법은 변수 = MemberManager() 생성

    # 클래스에서 self는 객체의 주소를 가지고 있음
    # def __init___(self) : 클래스 구현시 필수
    def __init__(self, file_name="member.txt"): # 객체생성시 만드는 기본값(생성자)
        self.file_name = file_name # 객체에 파일이름을 넣는다
        self.members = [] # 객체에 members 리스트를 만든다.
        self.session = None # 객체에 session 변수를 만들고 기본값으로 None 처리한다(int 타입)
        self.load_members() # 아래에 선언된 load_members() 메서드를 호출한다

    def load_members(self): # 앞으로 만들 메서드는 ()괄호 안에 self가 필수
        self.members = [] #  빈배열로 생성( 혹시나, 이전에 리스트가 남아있을 수 있음)

        if not os.path.exists(self.file_name): # 동일 디렉토리에 파일명이 없으면
            self.save_members() # save_members() 메서드 호출
            return # load_members()메서드로 빠져나오기
        with open(self.file_name, "r", encoding="utf-8") as f:
            #       members.txt   읽기전용         한글처리    f라는 변수
            for line in f: # f 변수에 있는 파일객체를 줄단위로 반복
                data = line.strip().split("|")
                # 1줄 읽은 값을 엔터제거 |를 기준으로 잘라 -> 1차원 리스트 생성
                data[4] = True if data[4] == "True" else False
                self.members.append(data)
    def save_members(self): # members 2차원 리스트 값을 파일로 덮어쓴다
        # 왜? 파일처리는 수정을 하지 않음
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members: # 메모리에 있는 members 2차원 리스트를 한 줄씩 가져와 member 변수에 넣기
                f.write(f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n")
    def member_add(self): # self는 클래스의 객체 주소
        print("\n[회원가입]")
        uid = input("ID : ") # 키보드로 입력한 값을 uid변수에 넣음
        for member in self.members: # 2차원 배열인 members에서 1차원 리스트 한줄을 가져오기
            if member[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return # member_add() 메서드를 빠져나옴
        # 중복 아이디가 없으면 아래쪽 코드 실행 -> else: 로 처리해도 가능 -> 들여쓰기 필수
        pw = input("Pw : ")
        name = input("Name : ")
        print("1.admin 2.manager 3.user")
        r = input("Role: ")
        role = "user"
        if r == "1":
            role = "admin"
        elif r == "2":
            role = "manager"
        # 여기까지가 변수에 입력 완료
        self.members.append([uid, pw, name, role, True])
        # 메모리에 있는 2차원 리스트에 members 뒤에 추가
        self.save_members() # 파일로 저장
        self.load_members()
        print("회원가입완료")
    def member_login(self):
        uid = input("ID : ")
        pw = input("Pw : ")

        # enumerate() -> 2차원 배열을 인덱스와 리스트를 추출
        for idx,member in enumerate(self.members):
        #   주소, 리스트
            if member[0] == uid: # for문 중에 같은 id가 있으면
                if not member[4]: # active가 false인지 확인
                    print("비활성화된 게정입니다.")
                    return # member_login()메서드를 빠져나옴

                # active가 True이면
                if member[1] == pw: # member[]
                    self.session = idx # session 변수에 인덱스를 넣는다
                    print(f"{member[2]}님 로그인 성공 ({member[3]})")
                    if member [3] == "admin": # 관리자이면
                        self.member_admin() # 관리자 메서드를 호출한다
                        return # member_login()메서드를 빠져나옴
                else: # member[1] == pw: 가 false라면
                    print("비밀번호 오류")
                    return # member_login()메서드를 빠져나옴
            else:
                print("존재하지 않는 아이디") # for문에 return이 안걸리면 여기까지 온다
    def member_admin(self): #로그인 시, role = admin이면 진입
        print("\n[관리자메뉴]")
        print("1.비밀번호변경")
        print("2.블랙리스트")
        print("3.권한변경")
        print("0.종료")

        select = input("선택 : ") # 관리자 메뉴 선택용
        if select == "0":
            return
        uid = input("관리 ID : ") # 대상 id 찾는용

        for member in self.members: # members에 2차원 배열을 반복
            if member[0] == uid: # 대상 id를 찾으면
                if select == "1":
                    member[1] = input("변경 비밀번호 : ")
                elif select == "2":
                    member[4] = False
                elif select == "3":
                    member[3] = input("admin, manager, user : ")
                self.save_members()
                self.load_members()
                print("관리자 작업 완료")
                return
        print("대상 회원 없음")
    def member_logout(self):
        self.session = None
        print("로그아웃 완료")
    def member_modify(self):
        if self.session is None:
            print("로그인 필요")
            return
        print("\n[내정보수정]")
        print("1. 이름변경")
        print("2. 비밀번호변경")

        select = input("선택 : ")
        if select == "1":
            self.members[self.session[2]] = input("새 이름 : ")
            #   2차원배열  로그인인덱스   이름필드
        elif select == "2":
            self.members[self.session[1]] = input("새 비밀번호 : ")
            #   2차원배열  로그인인덱스   암호필드
        self.save_members()
        self.load_members()
        print("수정완료")
    def member_delete(self):
        if self.session is None:
            print("로그인 필요")
            return
        print("\n[회원탈퇴]")
        print("1. 완전탈퇴")
        print("2. 계정 비활성화")

        select = input("선택 : ")
        if select == "1":
            self.members.pop(self.session)
        elif select == "2":
            self.members[self.session[4]] = False
        self.session = None
        self.save_members() # 파일로 저장
        self.load_members() # 다시 파일에 있는 내용을 불러옴
        print("처리 완료")
    def main_menu(self):
        print("""
    ==== 회원관리 프로그램 (Class기반) ====
    1. 회원가입 2. 로그인 3. 로그아웃
    4. 회원정보수정 5. 회원탈퇴 9. 종료
    """)
    def run(self):
        while True:
            self.main_menu()
            select = input("선택 : ")

            if select == "1": self.member_add()
            elif select == "2": self.member_login()
            elif select == "3": self.member_logout()
            elif select == "4": self.member_modify()
            elif select == "5": self.member_delete()
            elif select == "9": break
app = MemberManager() # 가장 중요한 포인트 (지금까지 만든 클래스를 객체로 만들고)
app.run() # 객체에 있는 .run() 메서드를 실행