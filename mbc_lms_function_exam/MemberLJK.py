run = True
session = None

ids = ["kkw","lhj","ljj"]
pws = ["1234","5678","8888"]
names = ["김기원","임효정","이재정"]
roles = ["admin","manager","user"]
active = [True,False,True]
blacklist = []

def member_login():
    #print("member login 함수에 진입합니다")
    global session
    if session is not None:
        print("이미 로그인 중입니다")
        print(f"{names[session]}님이 로그인중입니다")
        return
    else:
        user_id = input("아이디 : ")
        if user_id in ids:
            idx = ids.index(user_id)
            if active[idx] is False:
                print("비활성화 되어있는 아이디입니다")
                return
            else:
                user_pw = input("비밀번호 : ")
                if user_pw == pws[idx]:
                    session = idx
                    print("로그인 되었습니다")
                    print(f"{names[idx]}님 환영홥니다")
                    return
                else:
                    print("비밀번호가 일치하지 않습니다")
                    return
        else:
            print("아이디를 찾을 수 없습니다")
            return
    #print("member login 함수를 종료합니다")
def member_admin():
    if roles[session] != "admin":
        print("관리자만 이용가능합니다")
        return
    else:
        #print("member_admin 함수에 진입하였습니다")
        manage_user = input("회원 아이디 : ")
        idx = ids.index(manage_user)
        sub_menu3()
        if input(">>>") == "1":
            print("회원 상태 활성화 및 비활성화 메뉴입니다")
            if active[idx] is not True:
                if input(f"{names[idx]}님의 활동상태를 활성화 하시겠습니까? 맞으면 Y : ") == "y":
                    active[idx] = True
                    print(f"{names[idx]}님의 활동상태가 활성화 되었습니다")
                else:
                    print("다시 입력하세요")
                    return
            else:
                if input(f"{names[idx]}님의 활동상태를 비활성화 하시겠습니까? 맞으면 Y : ") == "y":
                    active[idx] = False
                    print(f"{names[idx]}님의 활동상태가 비활성화 되었습니다")
        elif input(">>>") == "2":
            print("회원 권한 관리 메뉴입니다")
            if roles[idx] == "manager":
                if input(f"{names[idx]}님의 권한을 일반사용자로 변경하시겠습니까? 맞으면 Y : ") == "y":
                    roles[idx] = "user"
                    print(f"{names[idx]}님의 권한이 일반사용자로 변경되었습니다")
                else:
                    print("다시 입력해주세요")
                    return
            else:
                if input(f"{names[idx]}님의 권한을 매니저로 변경하시겠습니까? 맞으면 Y : ") == "y":
                    roles[idx] = "manager"
        elif input(">>>") == "3":
            print("블랙리스트 관리 메뉴입니다")
            if input(f"{names[idx]}님을 블랙리스트에 추가하시겠습니까? 맞으면 Y : ") == "y":
                blacklist.append(ids[idx])
                active[idx] = False
                print(f"{names[idx]}님이 블랙리스트에 추가되셨습니다")
            else:
                print("다시 입력해주세요")
                return
    #print("member_admin 함수를 종료하였습니다")
def member_modify():
    if session is None:
        print("로그인 후 이용 가능합니다")
        return
    else:
        #print("member_modify 함수에 진입합니다")
        sub_menu2()

        sub_select2 = input(">>>")
        if sub_select2 == "1":
            change_name = input("변경하실 이름 : ")
            if input(f"변경하실 이름이 {change_name}이 맞으시면 Y : ") == "y":
                names[session] = change_name
                print(f"이름이 {names[session]}으로 변경되었습니다")
            else:
                print("다시 입력해주세요")
                return
        elif sub_select2 == "2":
            change_pw = input("변경하실 비밀번호 : ")
            if input(f"변경하실 비밀번호가 {change_pw}이 맞으시면 Y : ") == "y":
                pws[session] = change_pw
                print(f"비밀번호가 {pws[session]}으로 변경되었습니다")
            else:
                print("다시 입력해주세요")
                return
        elif sub_select2 == "9":
            return
        else:
            print("잘못 입력하셨습니다")
            return
    #print("member_modify 함수를 종료합니다")
def member_delete():
    if session is None:
        print("로그인 후 이용 가능합니다")
        return
    else:
        #print("member_delete 함수에 진입합니다")
        print("회원 탈퇴를 하시겠습니까?")
        if input("맞으면 Y : ") == "y":
            ids.pop(session)
            pws.pop(session)
            names.pop(session)
            roles.pop(session)
            active.pop(session)
            print("탈퇴가 완료되었습니다")
        else:
            print("다시 입력해주세요")
            return
    #print("member_delete 함수를 종료합니다")
def member_add():
    #print("member_add 함수에 진입합니다")
    new_id = input("아이디 : ")
    if new_id in ids:
        print("이미 존재하는 아이디입니다")
    else:
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        sub_menu()

        sub_select = input(">>>")
        if sub_select == "1":
            new_role = "admin"
        elif sub_select == "2":
            new_role = "manager"
        elif sub_select == "3":
            new_role = "user"
        else:
            "잘못 입력 하셨습니다"
        print(f"아이디 : {new_id} 비밀번호 : {new_pw} 이름 : {new_name} 권한 : {new_role}")
        if input("맞으면 Y를 눌러주세요 : ") == "y":
            print("저장 중입니다")
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_role)
            active.append(True)
            print("회원가입이 완료되었습니다")
            print(f"아이디 : {new_id} 비밀번호 : {new_pw} \n이름 : {new_name} 권한 : {new_role} 활동상태 : True")
            print(f"{new_name}님 환영합니다")
        else:
            "다시 입력해주세요"
            return
    #print("member_add 함수를 종료합니다")
def member_logout():
    global session

    if session is None:
        print("로그인 후 이용가능합니다")
        return
    else:
        #print("member_logout 함수에 진입하였습니다")
        if input("로그아웃 하겠습니까? 맞으면 Y : ") =="y":
            session = None
            print("로그아웃 되었습니다")
        else:
            print("다시 입력해주세요")
    #print("member_logout 함수를 종료합니다")
def member_end():
    global run
    if input("프로그램을 종료하시겠습니까? 맞으면 Y : ") == "y":
        run = False
def main_menu():
    print(f"""
========MBC 아카데미 회원관리 프로그램========
    1. 로그인  2. 회원가입 9. 프로그램 종료
==========================================
""")
def main_menu2():
    print(f"""
=======관리자 권한 메뉴=======
     1. 회원정보관리
2. 로그아웃   9. 프로그램 종료
============================
""")
def main_menu3():
    print(f"""
==========MY 페이지==========
1. 회원정보수정   2.회원탈퇴
3. 로그아웃   9. 프로그램 종료
============================
""")
def sub_menu():
    print(f"""
===========회원권한 확인===========
1. 관리자  2. 매니저   3. 일반사용자
=================================
""")
def sub_menu2():
    print(f"""
==============회원정보 수정==============
1. 이름 수정    2. 비밀번호 수정  9.뒤로가기
=======================================
""")
def sub_menu3():
    print(f"""
=================회원정보 수정=================
1. 회원 활성화/비활성화    2. 권한 수정  
3. 블랙리스트 관리         9.뒤로가기
=============================================
""")
while run:
    main_menu()
    select = input(">>>")
    if select == "1":
        member_login()
        if session is not None:
            if roles[session] == "admin":
                main_menu2()
                select2 = input(">>>")
                if select2 == "1":
                    member_admin()
                elif select2 == "2":
                    member_logout()
                elif select2 == "9":
                    member_end()
            elif roles[session] == "manager" or "user":
                main_menu3()
                select3 = input(">>>")
                if select3 == "1":
                    member_modify()
                elif select3 == "2":
                    member_delete()
                elif select3 == "3":
                    member_logout()
                elif select3 == "9":
                    member_end()

    elif select == "2":
        member_add()
    else:
        run = False