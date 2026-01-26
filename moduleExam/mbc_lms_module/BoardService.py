class BoardService:
    def __init__(self):
        lists = []
    def run(self):
        subrun3 = True
        while subrun3:
            print("""
==== 자료게시판 관리 메뉴 ====
1. 로그인
2. 새 글 등록
3. 리스트 보기
4. 글 수정
5. 뒤로가기
            """)
            subSelect3 = input("선택 : ")
            if subSelect3 == "1":
                print("로그인")
            elif subSelect3 == "2":
                print("새 글 보기 메뉴")
            elif subSelect3 == "3":
                print("리스트 보기 메뉴")
            elif subSelect3 == "4":
                print("글 수정 메뉴")
            elif subSelect3 == "5":
                print("뒤로가기")
                subrun3 = False
            else:
                print("잘못된 번호를 입력했습니다")
                print("다시 입력하세요")