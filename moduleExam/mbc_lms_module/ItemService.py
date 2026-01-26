import os


class ItemService:
    def __init__(self, file_name="item.txt"):
        # 클래시 생성시 필요한 변수들...
        self.file_name = file_name
        self.items = []
        self.load_item()
        self.session = None

    def load_item(self):
        self.items = []
        if not os.path.exists(self.file_name):
            self.save_items()
            return

        with open(self.file_name, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) >= 4:
                    self.items.append([data[4]])

    def save_items(self):
        with open(self.file_name, "w", encoding="utf-8", errors="replace") as f:
            for m in self.items:
                f.write("|".join(m[:4]) + "\n")

    # ------------------------------------------------------------------------------------------
    def full_view(self):
        print("교보재 전체 리스트 메서드 호출")
        print("교보재 전체 보기")
        print("no\t이름\t작성자\t출판사")
        for idx, item in enumerate(self.items, start=1):
            if len(item) < 4:
                print(f"{idx}\t{item[1]}\t{item[2]}\t{item[3]}")

    # ------------------------------------------------------------------------------------------
    def next_item_id(self):
        if not self.items:
            return 1
        return max(int(item[0]) for item in self.items) + 1

    def add_item(self):
        print("교보재 등록하기")
        new_id = self.next_item_id()
        une = input("교보재 이름 : ").strip()
        uwt = input("교보재 작성자 : ").strip()
        upb = input("교보재 출판사 : ").strip()

        self.items.append([str(new_id), une, uwt, upb])
        self.save_items()
        print("등록되었습니다")

    def find_item(self):
        name = input("교보재 이름 : ").strip()
        for m in self.items:
            if m[1] == name:
                if not m[1] == name:
                    print("해당하는 교보재가 없습니다.")
                    return
                else:
                    print(f"교보재 이름 : {m[1]}")
                    print(f"교보재 저자 : {m[2]}")
                    print(f"교보재 출판사 : {m[3]}")

    def stats_item(self):
        pass

    def logout_item(self):
        print("로그아웃 메서드 호출")
        yes = input("로그아웃 하려면 y를 눌러주세요 : ")
        if yes == "y":
            print("로그아웃 되었습니다.")
            self.session = None
        else:
            print("교보재 메뉴로 돌아갑니다.")
            pass

    def main_menu(self):
        print("""
------------------------------
1. 교보재 전체 리스트
2. 교보재 찾기
3. 교보재 이용 통계
4. 교보재 등록 하기
5. 로그아웃

8. 교보재 종료
9. 엠비씨 LMS 서비스 종료
""")

    # ------------------------------------------------------------------------------------------
    def run(self):
        # 부메뉴 구현 메서드
        subrun = True
        while subrun:
            self.main_menu()

            subSelect = input(">>> ")
            if subSelect == "1":
                self.full_view()

            elif subSelect == "2":
                self.find_item()

            elif subSelect == "3":
                self.stats_item()

            elif subSelect == "4":
                self.add_item()

            elif subSelect == "5":
                self.logout_item()

            elif subSelect == "8":
                print("교보재 메뉴 종료")
                subrun = False

            elif subSelect == "9":
                print("엠비씨 LMS 서비스 종료")
                exit()

            else:
                print("잘못된 메뉴를 선택하셨습니다.")
