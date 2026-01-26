# 주민번호를 입력받아 생년월일, 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0 : 주민번호 입력 검증 - 14글자인지, 7번째에 -가 있는지
# 처리1 : 생년월일을 추출 -> 1,2,5,6 1900년생, 나머지 2000년생
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여 구분
# 처리3 : 9~10번째 글자를 추출 -> 출생지역 구분

print("주민번호를 입력하세요.(-포함 14자)")
ssn = input(">>>")
# 입력된 주민번호 검증 코드
if len(ssn)==14: #키보드로 입력된 문자열이 14자인지 확인
    print("14자 입력이 확인되었습니다.")
    if ssn[6] == "-":
        print("주민번호 7번째 구문자 인식완료")
    else:
        print("주민번호 7번째 구문자가 입력되지 않았습니다.")
        print("프로그램을 처음부터 다시 실행하세요.")
        exit(0)
else:
    print("주민번호 14자가 입력되지 않았습니다.")
    exit(0) #강제종료
# if ssn[6] == "-":
    print("주민번호 7번째 구문자 인식완료")
# else:
    print("주민번호 7번째 구문자가 입력되지 않았습니다.")
    print("프로그램을 처음부터 다시 실행하세요.")
    exit(0)
# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생
# 나머지는 2000년생
print("입력된 주민번호 : "+ssn)
print("이름을 입력하세요.")
name = input(">>>")
print("입력된 이름 : "+name)
year = ssn[0:2] # 생년
month = ssn[2:4] # 생월
day = ssn[4:6] # 생일
# print(year)
# print(month)
# print(day)
num = ssn[7]
num = int(num)
# if num%2==1:
    # sex = "남자"
# else:
    # sex = "여자"
# print(sex)
fullYear = "" # if 안족에서 변수를 만들면 버그가 생길 수가 있음
if ssn[7] in ["1","2","5","6"]:
    fullYear = "19"+year
else:
    fullYear = "20"+year
# 나이 계산
age = 2026-int(fullYear)
age = str(age)
#           pint는 문자열 + 숫자로 출력 오류가 발생
#                   문자열로 변환(강제타입변화) -> str(age)
if ssn[8] in ["1","3","5","7"]:
    gender = "남성"
elif ssn[8]=="9":
    gender = "외계인"
else:
    gender = "여성"
home = ssn[8:10]
home = int(home)
if home <= 8:
    home = "서울"
elif home <= 12:
    home = "부산"
elif home <= 15:
    home = "인천"
elif home <= 25:
    home = "경기도"
elif home <= 34:
    home = "강원도"
elif home <= 47:
    home = "충청도"
elif home <= 66:
    home = "전라도"
elif home <= 91:
    home = "경상도"
else:
    home = "제주도"

print(name+"님은 "+fullYear+"년 "+month+"월 "+day+"일에 태어난 "+age+"세 "+home+" "+gender+"입니다.")

# 주민번호 8번째 숫자가 1,3,5,7 이면 남자, 나머지는 여자
# 8~9번째
# 서울 00-08 부산 09-12 인천 13-15 경기 16-25 강원 26-34 충청 35-47 전라 48-66 경상 67-91 제주 92-95