# 회원관리용 더미데이터를 파일(txt)로 저장하여 관리
import os

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt" # 회원정보를 저장할 메모장 파일명
members = [] # 지금은 비어있지만 좀 있다 메모장에 있는 내용을 가져와 리스트 처리
# members 구조 :
# [아이디, 비밀번호, 이름, 권한, 활성화여부]
#  "kkw"  "1234""김기원""admin""True"
#  kkw|1234|김기원|admin|True 로 메모장에 저장될 예정

# 파일 처리용 함수들
def save_members(): # 메모리상에 리스트를 파일로 저장
    """
    members 리스트 내용을 members.txt 파일엘 저장
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        #       상수     덮어쓰기        한글처리용   파일객체
        #                a = 추가
        # 메모리에 있는 리스트를 |로 연결하여 한줄로 저장
        for member in members:
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            #               kkw|       1234|       김기원|       admin|         True
            f.write(line)
# save_members() 함수 종료

def load_members(): # txt파일을 전체 불러와 리스트로 만드는 것, 중간 수정이 안됨
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """
# 파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME): # 지금 디렉토리에 FILE_NAME이 없으면
        # os.path. : 현재 위치 -> os : 내부 라이브러리지만 기본적으로 포함하지 않아 import 해야함
        save_members() # 빈 파일이 members.txt로 생성
        return

# 있으면 파일을 열어서 한줄 씩 읽기
with open(FILE_NAME, "r", encoding="utf-8") as f:
    for line in f: # f 파일내용을 한줄씩 line 변수에 넣음
        print(f"변조 전 데이터 : {line}")

        # 줄 끝에 엔터 제거, |로 분류된거 리스트화
        data = line.strip().split("|")
        #          맨뒤 엔터제거
        #                       |를 기준으로 나누기

        # 변조 후 데이터를 확인해보면 모두 다 문자열로 취급됨
        # 문자열 True를 블리언(True/False) 타입으로 변환
        data[4] = True if data[4] == "True" else False
        # 받는변수   넣을값     data 4번째 가 문자열 True이면
        #                                   아니면 False
        # if data[4] == "True":
        #    data[4] = True
        # else:
        #    data[4] = False
        print(f"변조 후 데이터 ; {data}")
        print("----------------------")

        # 마지막 members 리스트에
        members.append(data)


# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    print("회원가입 메뉴입니다")
    # 회원가입에 필요한 기능을 넣음
    uid = input("ID : ")
    # 아이디 중복검사
    for member in members:
        if member[0] == uid: # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}
            #                       uid       upw         uname       role       active
            print("이미 존재하는 아이디입니다")
            return # 돌아감
    upw = input("Password : ")
    uname = input("Name : ")
        # 권한선택
    print("1.admin 2.manager 3.user ")
    role = input("Role: ")
    role = "user" # 잘못 클릭해도 user 권한으로 기본값 설정
    if role == "1":
        role = "admin"
    elif role == "2":
        role = "manager"
     # ====== 입력 종료 =========
    print(f"ID : {uid} Name : {uname}")
    print(f"Role : {role} Password : {upw}")
    # ====== 입력값 확인 ========

    save_True = input("저장하려면 Y를 누르세요 : ")
    if save_True == "y":
        # 저장 시작
        members.append([uid,upw,uname,role,True]) # 리스트화
        save_members() # 파일화
        print("회원가입완료")

# member_add() 함수 종료
# 회원가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    global session
    i = 0
    user_id = input("ID : ").strip()
    if user_id = [0]

    # 로그인에 필요한 기능을 넣음

    print("member_login 함수를 종료합니다.")


# 회원로그인용 함수 종료

def member_admin():
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드

    # 블랙리스트로 변환 -> active를 False

    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")


# 관리자가 사용자 변경사항 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경

    print("member_logout 함수를 종료합니다.")


# 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.

    print("member_modify 함수를 종료합니다.")


# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)

    print("member_delete 함수를 종료합니다.")


# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입    2. 로그인     3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴
    9. 프로그램 종료
    """)


# 메인메뉴용 함수 종료

def member_add_menu():  # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요.---------
    1. 관리자    2. 팀장    3. 일반사용자 
    """)


# ------------------ 메뉴 함수 끝 ------------------

# 프로그램 시작!!!!
load_members() # 프로그램 시작 시 파일 불러오기
print(members)
while run:  # 메인 프로그램 실행 코드
    main_menu()  # 위에서 만든 메인 메뉴함수를 실행
    select = input(">>>")  # 키보드로 메뉴 선택
    if select == "1":  # 회원가입 코드
        member_add()  # 회원가입용 함수 호출

    elif select == "2":  # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5":  # 회원탈퇴 선택
        member_delete()  # 회원정보 삭제 함수 호출

    elif select == "9":  # 프로그램 종료 선택
        run = False

    else:
        print("잘못 입력하셨습니다.")
# while문 종료