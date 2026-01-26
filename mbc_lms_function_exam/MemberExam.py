# 회원관리 crud를 사용자 지정 함수로 만들어보자
# c : 회원가입
# r : 회원리스트 (관리자인 경우) 회원암호 변경, 블랙리스트 생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화
from psutil import users

# 프로그램에서 사용될 변수들
# 전역 변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역 변수(local) -> while, if, for, def 안에서 사용되는 변수
run = True # while에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용

# 프로그램에서 사용될 리스트들 (더미 데이터)
# sns = [1,2,3] # 회원번호 들 (회원삭제 및 추가 시, 번호가 흔들릴 수 있음(인덱스로만)
ids = ["kkw","lhj","ljj"] # 로그인 아이디 들
pws = ["1234","5678","8888"] # 로그인 암호 들
names = ["김기원","임효정","이재정"] # 사용자 명 들
roles = ["admin","manager","user"] # 사용자 권한 들 (admin, manager, user)
active = [True,True,True] # 회원사용중, 탈퇴, 중지, 블랙리스트 등 (True, False)
# 차후에는 파일처리로 변환 할 예정

# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다")
    # 회원가입에 필요한 기능을 넣음
    new_id = input("아이디 : ") # 키보드로 아이디를 넣음
    # 이미 아이디가 존재하면 다른 아이디를 넣게 유도
    if new_id in ids: # ids : 아이디 들, ids 리스트에 new_id가 있는지 확인
        # True 일 때,
        print("이미 존재하는 아이디입니다")
        return # if문 종료
    else: # False 일 때, ids에 new_id가 없을 때 (중복이 없다)
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        member_add_menu() # 회원권한 메뉴 출력

        role_set = input("권한 선택 : ")
        if role_set == "1":
            new_role = "admin"
        elif role_set == "2":
            new_role = "manager"
        else:
            new_role = "user"
        print(f"""
입력된 정보를 확인하세요
이름 : {new_name} 암호 : {new_pw}
아이디 : {new_id} 권한 : {new_role}
""")
        save_select = input("저장하려면 Y : ")
        if save_select == "y":
            print("저장하는 중입니다")
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_role)
            active.append(True)  # 저장완료
            print("회원가입이 완료되었습니다")

            # 차후에 로그인 함수를 추가
        else:
            print("회원가입이 되지 않았습니다")
    print("member_add 함수를 종료합니다")
    # 회원가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다")
    # 로그인에 필요한 기능을 넣음
    global session  # 맨 위에 전역변수로 지정한 내용 활용

    if session is not None: # session에 이미 값이 있으면
    # if session is not None -> 객체 비교할 때
    # if session != None -> 숫자 비교할 때
        #True
        print("이미 로그인 한 상태입니다")
        print(f"로그인한 사용자는 {names[session]}님 입니다")
        return # if문 종료
    else:
        #False
        user_id = input("아이디 : ")
        if user_id in ids: #키보드로 받은 아이디가 ids 리스트에 있는지 확인
            #True 있으면
            idx = ids.index(user_id)
            if not active [idx]: #회원 활성화 상태인지 확인
                #False
                print("비활성화 혹은 차단된 계정입니다")
                return
            else:
                #True
                # 암호 비교
                user_pw = input("비밀번호 : ")
                if user_pw == pws[idx]: #키보드로 넣은 암호와 pws 리스트의 주소 암호가 일치하는지 확인
                    # id도 같고 활성화 상태이고 암호가 같다
                    session = idx # 로그인 상태
                    # 글로벌 영역의 session값(로그인한 사용자의 주소)이 있는 상태
                    print(f"{names[session]}님 환영합니다")
                    print(f"{roles[idx]} 권한을 가지고 있습니다")
                else:
                    print("비밀번호가 일치하지 않습니다")
        else:
            #False 없으면
            print("존재하지 않는 아이디입니다")
    print("member_login 함수를 종료합니다")
    # 회원로그인용 함수 종료

def member_admin():
    # 관리자가 로그인 했을 경우 하 수 잇는 기능을 작성
    print("member_admin 함수로 진입합니다")
    # 다른 사용자 암호 변경 코드
    # 블랙리스트로 변환할 수 있는 코드 -> active를 False
    # 권한 부여 -> 사용자의 권한을 변경 (roles를 변경) manager <-> user
    print("member_admin 함수를 종료합니다")
    # 관리자가 로그인 했을 경우의 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다")
    # 로그인 상태인지 확인, session을 None으로 변경
    print("member_logout 함수를 종료합니다")
    # 로그아웃 함수를 종료

def member_modify():
    # 회원정보 수정 함수
    print("member_modify 함수로 진입합니다")
    # 로그인 상태인지를 확인하고 자신의 정보를 확인하고 수정한다
    print("member_modify 함수를 종료합니다")
    # 회원정보 수정 함수 종료

def member_delete():
    # 회원 탈퇴 및 회원 유휴 등 처리하는 함수
    print("member_delete 함수로 진입합니다")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴는 active를 False처리
    print("member_delete 함수를 종료합니다")
    # 회원 탈퇴 및 유휴 처리 함수 종료

# ------------------------------기능에 대한 함수 생성------------------------------

def main_menu():
    print(f"""
    ===== MBC 아카데미 회원가입 프로그램 =====
    1. 회원가입     2. 로그인      3. 로그아웃
    4. 회원정보수정       5. 회원탈퇴
    9. 프로그램 종료
    """)
    # 메인메뉴용 함수 종료

def member_add_menu():
    # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요 -----
    1. 관리자  2. 팀장   3. 일반 사용자
    """)

# ------------------------------ 메뉴 함수 끝 ------------------------------

# 프로그램 시작
while run: # 메인 프로그램 실행 코드
    main_menu() # 위에서 만든 메인 메뉴를 실행
    select = input(">>>") # 키보드로 메뉴 선택
    if select == "1": # 회원가입 메뉴 선택
        member_add() # 회원가입용 함수 호출
    elif select == "2": # 로그인 메뉴 선택
        member_login() # 로그인용 함수 호출
    elif select == "3": # 로그아웃 메뉴 선택
        member_logout() # 로그아웃 함수 호출
    elif select == "4": # 회원정보수정 메뉴 선택
        member_modify() # 회원정보수정 함수 호출
    elif select == "5" : # 회원탈퇴 메뉴 선택
        member_delete() # 회원탈퇴 함수 호출
    elif select == "9": # 프로그램 종료 메뉴 선택
        run = False # while문 종료
    else:
        print("잘못 입력하셨습니다")