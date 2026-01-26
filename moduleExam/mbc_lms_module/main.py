# 주실행 코드로 주메뉴를 담당한다
# 외부 모듈을 호출해서 연동한다
import MemberService # 회원관리용 클래스
import ScoreService # 점수관리용 클래스
import BoardService # 게시판관리용 클래스
import ItemService # 상품관리용 클래스


def main():
    run = True
    while run:
        print(f"""
========MBC 아카데미 LMS 프로그램========
1. 회원관리
2. 성적관리
3. 자료게시판
4. 교보재관리
5. 교수전용
6. 취업용게시판
9. 종료
""")
        select = input("선택 : ")
        if select == "1":
            print("회원관리 서비스로 진입합니다")
            # 회원관리 서비스 호출 코드
            MemberService.MemberService().run()
            # import명       클래스명       메서드
            print("회원관리 서비스를 종료합니다")
        elif select == "2":
            print("성적관리 서비스로 진입합니다")
            # 성적관리 서비스 호출 코드
            ScoreService.ScoreService().run()
            print("성적관리 서비스를 종료합니다")
        elif select == "3":
            print("자료게시판 서비스로 진입합니다")
            # 자료게시판 서비스 호출 코드
            BoardService.BoardService().run()
            print("자료게시판 서비스를 종료합니다")
        elif select == "4":
            print("교보재관리 서비스로 진입합니다")
            # 교보재관리 서비스 호출 코드
            ItemService.ItemService().run()
            print("교보재관리 서비스를 종료합니다")
        elif select == "5":
            print("교수전용 서비로 진입합니다")
            # 교수전용 서비스 호출 코드
            print("교수전용 서비를 종료합니다")
        elif select == "6":
            print("춰업용게시판 서비스로 진입합니다")
            # 취업용게시판 서비스 호출 코드
            print("춰업용게시판 서비스를 종료합니다")
        elif select == "9":
            print("종료")
            run = False
        else:
            print("잘못된 번호를 입력하셨습니다")
            print("다시 입력하세요")

if __name__ == "__main__":
    # 여러 파일을 호출하기 때문에 main일 때만 main()메서드를 실행
    main() # 위에 만든 main()함수를 실행