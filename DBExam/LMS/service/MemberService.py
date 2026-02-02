from LMS.common.Session import Session
from LMS.domain.Member import Member


class MemberService:
    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("select count(*) as cnt from members")
                count = cursor.fetchone()['cnt']
                print(f"시스템에 등록된 회원 수는 {count}명 입니다.")
        except:
            print("MemberService.load()메서드 실행오류...")
        finally:
            print("데이터베이스 접속종료...")
            conn.close()
    @classmethod
    def login(cls):
        print("[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = 'select * from members where uid = %s and password = %s'
                cursor.execute(sql, (uid, pw))
                row = cursor.fetchone()
                if row:
                    member = Member.from_db(row)
                    if not member.active:
                        print("비활성화 계정입니다. 관리자에게 문의하세요.")
                        return
                    Session.login(member)
                    print(f"{member.name}님 로그인 성공 {member.role}")
                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")
        except:
            print("MemberService.login()메서드 실행오류...")
        finally:
            conn.close()
    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("[알림] 현재 로그인 상태가 아닙니다.")
            return
        Session.logout()
        print("[성공] 로그아웃이 완료되었습니다. 안녕히 가세요!")
    @classmethod
    def signup(cls):
        print("[회원가입]")
        uid = input("아이디 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                check_sql = 'select * from members where uid = %s'
                cursor.execute(check_sql, (uid,))
                if cursor.fetchone():
                    print("이미 존재하는 아이디입니다.")
                    return
                pw = input("비밀번호 : ")
                name = input("이름 : ")
                insert_sql = 'insert into members (uid, password, name) values (%s, %s, %s)'
                cursor.execute(insert_sql, (uid, pw, name))
                conn.commit()
                print("회원가입 완료! 로그인해주세요!")
        except Exception as e:
            conn.rollback()
            print(f"회원가입 오류 : {e}")
        finally:
            conn.close()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        member = Session.login_member
        print(f"내정보확인 : {member}")  # Member.__str__()
        print("\n[내 정보 수정]\n1. 이름 변경  2. 비밀번호 변경 3. 계정비활성 및 탈퇴 0. 취소")
        sel = input("선택: ")
        new_name = member.name
        new_pw = member.pw

        if sel == "1":
            new_name = input("새 이름 : ")
        elif sel == "2":
            new_pw = input("새 비밀번호 : ")
        elif sel == "3":
            cls.delete()
        else:
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = 'update members set name = %s, password = %s where uid = %s'
                cursor.execute(sql, (new_name, new_pw, member.id))

                member.name = new_name
                member.pw = new_pw
                print("정보 수정 완료!")
        finally:
            conn.close()

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        member = Session.login_member
        print("\n[회원 탈퇴]\n1. 완전 탈퇴  2. 계정 비활성화")
        sel = input("선택: ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = 'delete from members where uid = %s'
                    cursor.execute(sql, (member.id,))
                    print("회원 탈퇴 완료!")
                elif sel == "2":
                    sql = 'update members set member.active = false where uid = %s'
                    cursor.execute(sql, (member.id,))
                    print("계정 비활성화 완료!")

                conn.commit()
                Session.logout()
        finally:
            conn.close()

    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.is_admin():
            print("관리자 전용 메뉴입니다.")
            return
        print("""
            [관리자 메뉴]
            1. 회원리스트 조회
            2. 회원 권한 수정
            3. 블랙리스트 관리
            0. 뒤로가기
            """)
        sel = input("선택 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    print("[회원리스트 조회]")
                    sql = 'select * from members'
                    cursor.execute(sql)
                    line = cursor.fetchall()
                    for f in line:
                        if f['active'] == 1:
                            f['active'] = True
                        else:
                            f['active'] = False
                        print(f"회원번호 : {f['id']}|"
                              f"아이디 : {f['uid']}|"
                              f"이름 : {f['name']}|"
                              f"권한 : {f['role']}|"
                              f"활성 : {f['active']}")
                elif sel == "2":
                    print("[회원 권한 수정]")
                    uid = input("대상 아이디 : ")
                    sel2 = input("admin / manager / user : ").lower()
                    if sel2 == "admin":
                        sql = 'update members set role = "admin" where uid = %s'
                        cursor.execute(sql, (uid,))
                    elif sel2 == "manager":
                        sql = 'update members set role = "manager" where uid = %s'
                        cursor.execute(sql, (uid,))
                    elif sel2 == "user":
                        sql = 'update members set role = "user" where uid = %s'
                        cursor.execute(sql, (uid,))
                    conn.commit()
                    print("권한 수정 완료")
                elif sel == "3":
                    print("[블랙리스트 관리]")
                    uid = input("대상 아이디 : ")
                    sql = 'update members set active = False where uid = %s'
                    cursor.execute(sql, (uid,))
                    conn.commit()
                    print("블랙리스트 관리 완료")
        except:
            print("MemberService.admin_menu()메서드 오류발생..")
        finally:
            conn.close()