# 파이썬에 oop를 적용하기
# oop : 객체 지향 프로그래밍, Object-Oriented Programing
# 현실 세계의 '객체' 개념을 기반으로 테이터를 속성(데이터)과
# 행위(메서드)로 묶어 관리하고
# 객체 간 상호작용을 통해 프로그램을 설게하는 프로그래밍 패러다임으로
# 코드 재사용, 유지보수 용이성, 가독성 향상 등의 장점이 있으며
# 캡슐화, 상속, 다형성 등의 핵심 원칙을 가짐

# 지금까지는 2차원 배열을 이용해서 인덱스로 데이터에 접근을 하는데
# 메모장 1줄로 되어있는 자료를 클래스로 만들면
# Member.name / Member.id / Member.pw 등으로 접근할 수 있음

# Member.py는 개인의 객체 -> 변수와 게터(나오는값)/세터(입력값) 등을 담당
# MemberService.py는 crud용 메서드들이 들어있는 모듈
# main.py는 주 실행코드


from MemberService import MemberService
#  외부파일(모듈) 가져오기     클래스 연결

app = MemberService() # 회원서비스 클래스를 app이라는 변수에 연결
app.run() # app 변수에 연결된 클래스 안에 run()메서드를 실행