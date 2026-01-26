names = []
births = []
nums = []
ids = []
pws = []
emails = []
admins = []

menu = """
==========================
MBC 아카데미 회원관리 프로그램
==========================
1. 로그인
2. 회원 정보 조회
3. 회원 정보 수정
4. 회원 탈퇴
5. 회원 가입
6. 종료
"""

run = True
login_user = None

while True:
    print(menu)
    print("안녕하세요 MBC 아카데미 회원관리 프로그램입니다")
    select = input("메뉴를 선택해주세요 : ")
    if select == "1":
        print("로그인 메뉴입니다")
        log_id = input("아이디를 입력해주세요 : ")
        login_user = ids.index(log_id)
        if log_id in ids[0:]:
            log_pw = input("비밀번호를 입력하세요 : ")
            if log_pw == pws[login_user]:
                print("로그인 되었습니다")
            else:
                print("비밀번호가 일치하지 않습니다")
        else:
            print("아이디를 찾을 수 없습니다")
    elif select == "2":
        if login_user is None:
            print("로그인 후 사용 가능합니다")
            continue

        print("회원 정보 조회 메뉴입니다")
        print("\n내정보")
        print(f"이름 : {names[login_user]} | 생년월일 : {births[login_user]} | 전화번호 : {nums[login_user]}")
        print(f"ID : {ids[login_user]} | Password : {pws[login_user]} | Email : {emails[login_user]}")

    elif select == "3":
        if login_user is None:
            print("로그인 후 사용 가능합니다")
            continue

        print("회원 정보 수정 메뉴입니다")
        nums[login_user] = input("전화번호 변경 : ")
        pws[login_user] = input("비밀번호 변경 : ")
        emails[login_user] = input("이메일 변경 : ")
        print("변경 전화번호 : "+nums[login_user])
        print("변경 비밀번호 : "+pws[login_user])
        print("변경 이메일 : "+emails[login_user])
        print("입력하신 정보가 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ") == 'y':
            print("변경되었습니다")
        else:
            print("다시 입력해주세요")
    elif select == "4":
        if login_user is None:
            print("로그인 후 사용 가능합니다")
            continue

        print("회원 탈퇴 메뉴입니다")
        print("탈퇴하시겠습니까? 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ") == 'y':
            names.pop(login_user)
            births.pop(login_user)
            nums.pop(login_user)
            ids.pop(login_user)
            pws.pop(login_user)
            emails.pop(login_user)
            admins.pop(login_user)
            print("탈퇴가 완료되었습니다")
        else:
            continue

    elif select == "5":
        print("회원 가입 메뉴입니다")
        name = input("이름은 입력하세요 : ")
        birth = input("생년월일을 입력하세요 : ")
        num = input("전화번호를 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        admin = False
        print("이름 : "+name)
        print("생년월일 : "+birth)
        print("전화번호 : "+num)
        print("아이디 : "+id)
        print("비밀번호 : "+pw)
        print("이메일 : "+email)
        print("입력하신 정보가 맞으신가요? 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ") == "y":
            names.append(name)
            births.append(birth)
            nums.append(num)
            ids.append(id)
            pws.append(pw)
            emails.append(email)
            admins.append(admin)
            print("회원가입이 완료되었습니다")
        else:
            print("다시 입력해주세요")
    elif select == "6":
        print("프로그램을 종료합니다")
        run = False
    else:
        "1~6번 메뉴에서 골라주세요"

