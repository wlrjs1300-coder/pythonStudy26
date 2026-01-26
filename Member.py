# 회원관리용 코드를 만든다.
# c -> 회원추가
# r -> 관리자일경우 (전체회원보기), 일반회원일경우 (로그인)
# u -> 관리자일경우 (회원차단, 암호변경문의), 일반회원일경우(내정보수정, 암호변경)
# d -> 회원탈퇴

# 메뉴구현
menu = """
==========================
MBC 아카데미 회원관리 프로그램
==========================
1. 로그인
2. 회원정보확인
3. 회원정보수정
4. 회원가입
5. 탈퇴
6. 종료
"""

names = ["alex","bob","cole"]
births = ["950810","260106","050505"]
ids = ["a","b","c"]
pws = ["1234","4567","7890"]
emails = ["alex@mbc.com","bob@mbc.com","cole@mbc.com"]
admins = [True, False, False]

run = True
login_user = None

while run:
    print(menu)
    select = input("원하시는 서비스를 선택해주세요 : ")
    if select == "1":
        log_id = input("아이디를 입력하세요 : ")
        if log_id in ids[0:]:
            login_user = ids.index(log_id)
            log_pw = input("비밀번호를 입력하세요 : ")
            if log_pw == pws[login_user]:
                print("로그인에 성공하였습니다")
                continue
            else:
                print("비밀번호가 일치하지 않습니다")
        else:
            print("아이디를 찾을 수 없습니다")
    if select == "2":
        if login_user is None:
            print("로그인 후 이용 가능합니다")
            continue

        if admins[login_user]:
            print("\n전체회원목록")
            for i in range(len(ids)):
                print(f"{i+1}. {names[i]} | {births[i]} | {admins[i]}")
        else:
            print("\n내정보")
            print(f"{names[i]} | {births[i]} | {admins[i]}")
    elif select == "3":
        if login_user is None:
            print("로그인 후 이용 가능합니다")
            continue

        print("\n내정보 수정")
        print("1. 이름 변경")
        print("2. 비밀번호 변경")
        print("3. 이메일 변경")

        choice = input("원하시는 서비스를 선택해주세요 : ")
        if choice == "1":
            names[login_user] = input("변경하실 이름을 입력해주세요 : ")
            print("이름 변경 완료 : "+names[login_user])
        elif choice == "2":
            pws[login_user] = input("변경하실 비밀번호를 입력해주세요 : ")
            print("비밀번호 변경 완료 : "+pws[login_user])
        else:
            emails[login_user] = input("변경하실 이메일을 입력해주세요 : ")
            print("이메일 변경 완료 : "+emails[login_user])
    elif select == "4":
        print("회원가입을 진행하겠습니다")
        name = input("이름을 입력하세요 : ")
        birth = input("생년월일을 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        admin = False

        print("이름 : "+name)
        print("생년월일 : "+birth)
        print("아이디 : "+id)
        print("비밀번호 : "+pw)
        print("이메일 : "+email)
        print("입력하신 정보가 맞으시면 Y, 틀리시면 N을 눌러주세요")

        if input("Y/N")=="Y":
            print("회원가입이 완료되었습니다")
        else:
            print("다시 입력해주세요")
    elif select == "5":
        if login_user is None:
            print("로그인 후 이용 가능합니다")
            continue
        print("탈퇴하시겠습니까? 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ")=="y":
            names.pop(login_user)
            births.pop(login_user)
            ids.pop(login_user)
            pws.pop(login_user)
            emails.pop(login_user)
            admins.pop(login_user)
            print("탈퇴하였습니다. 감사합니다")
        else:
            continue
    else:
        print("프로그램을 종료합니다. 감사합니다")
        run = False