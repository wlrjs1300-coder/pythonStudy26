# 성적 처리용 프로그램을 개발해보자

# CREATE : 성적입력
# READ : 성적조회
# UPDATE : 성적수정
# DELETE : 성적삭제

# 필요한 변수
sns = [] #학번
names = [] #이름
kors = [] #국어점수
engs = [] #영어점수
mats = [] #수학점수
tots = [] #빈 배열, 총점
avgs = [] #빈 배열, 평균
grades = [] #빈 배열, 학점

menu = """
==========================
MBC 아카데미 성적관리 프로그램
==========================

1. 성적 입력
2. 성적 보기
3. 성적 수정
4. 성적 삭제
5. 프로그램 종료

"""

run = True # 프로그램 실행중
login_user = None
login_user2 = None

while run: # run 변수가 False 처리 될 때까지 반복
    # : 아래는 들여쓰기 4칸정도 처리
    # 들여쓰기를 진행하면 하위 실행문
    print(menu) #콘솔창에 메뉴 출력
    select = input("원하는 메뉴를 선택하세요 : ") # select 변수에 숫자를 넣는다
    #               키보드로 입력받는 곳 앞쪽에 출력 메세지
    if select == "1": # 키보드로 입력한 숫자가 1이면
        print("성적 입력 메뉴를 선택하셨습니다") #1일 때 처리되는 부분
        sn = input("학번을 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        kor = int(input("국어 점수를 입력하세요 : "))
        eng = int(input("영어 점수를 입력하세요 : "))
        mat = int(input("수학 점술르 입력하세요 : ")) # 키보드를 이용한 점수 입력
        print("입력한 정보를 확인합니다")
        print(f"학번 : {sn}")
        print(f"이름 : {name}")
        print(f"국어 점수 : {kor}")
        print(f"영어 점수 : {eng}")
        print(f"수학 점수 : {mat}")
        print("입력하신 점수가 맞으면 Y, 틀리면 N을 눌러주세요")
        if input("Y/N : ") == "y":
            tot = kor + eng + mat
            avg = tot / 3
            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            elif avg >= 60:
                grade = "D"
            else:
                grade = "F"
            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat)
            tots.append(tot)
            avgs.append(avg)
            grades.append(grade) # 변수 뒤에 s는 배열(리스트)라고 생각
                                 # 변수.append() 리스트 뒤에 값이 추가됨
            print("성적 입력이 완료되었습니다")
        else:
            print("다시 입력하세요")
    elif select == "2": #키보드가 입력한 숫자가 2이면
        print("성적 조회 메뉴를 선택하였습니다")

        # for i in range(len(sns)) # 리스트의 처음부터 끝까지 반복용
            #          len(sns) -> sns 리스트의 길이를 가져옴
            #    range(len(sns)) -> 0부터 len(sns)
        log_sn = input("학번을 입력하세요 : ")
        login_user = sns.index(log_sn)
        print(f"학번 : {sns[login_user]} | 이름 : {names[login_user]}")
        print(f"국어 : {kors[login_user]} | 영어 : {engs[login_user]} | 수학 : {mats[login_user]}")
        print(f"총점 : {tots[login_user]} | 평균 : {avgs[login_user]} | 학점 : {grades[login_user]}")
        print("=============================================")
    elif select == "3":
        print("성적 수정 메뉴를 선택하였습니다")
        sn = input("학번을 입력해주세요 : ")

        if sn in sns :
            print("학번이 확인되었습니다")
            idx = sns.index(sn) # 찾은 학번의 주소
            print(f"이름 : {names[idx]} | 국어 : {kors[idx]} | 영어 : {engs[idx]} | 수학 : {mats[idx]}")

            kors[idx] = int(input("수정할 국어 점수 : "))
            engs[idx] = int(input("수정할 영어 점수 : "))
            mats[idx] = int(input("수정할 수학 점수 : "))
            tots[idx] = kors[idx] + engs[idx] + mats[idx]
            avgs[idx] = tots[idx] / 3
            if avgs[idx] >= 90:
                grades[idx] = "A"
            elif avgs[idx] >= 80:
                grades[idx] = "B"
            elif avgs[idx] >= 70:
                grades[idx] = "C"
            elif avgs[idx] >= 60:
                grades[idx] = "D"
            else:
                grades[idx] = "F"
        else:
            print("학번이 확인되지 않습니다")
            print("처음으로 돌아갑니다")
    elif select == "4":
        print("성적 삭제 메뉴를 선택하였습니다")
        sn = input("학번을 입력하세요 : ")
        if sn in sns :
            print("학번이 확인되었습니다")
            idx = sns.index(sn)
            if input("성적을 삭제 하시겠습니까? 맞으면 Y, 아니면 N을 눌러주세요 : ") == "y":
                sns.pop(idx)
                names.pop(idx)
                kors.pop(idx)
                engs.pop(idx)
                mats.pop(idx)
                tots.pop(idx)
                avgs.pop(idx)
                grades.pop(idx)
                print("삭제가 완료되었습니다. 감사합니다")
        else:
            print("학번을 찾을 수 없습니다")
    elif select == "5":
        print("프로그램 종료 메뉴를 선택하였습니다")
        print("프로그램을 종료합니다")
    else:
        print("똑바로 입력하세요")
