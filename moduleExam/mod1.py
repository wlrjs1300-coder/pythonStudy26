# 모듈 학습하기
# 모듈은 파이썬 파일로 만든 것을 연동하여 프로그램으로 처리한다
# 실무에서는 파일 한개로 모두 만들어 제공하는 것이 아니라
# 각각 기능이 있는 파일을 빼서 클래스화 하고 메서드로 동작한다
# Main.py -> __name__ (__main__)주 실행코드와 서비스를 연결하는 주메뉴와 메서드
# MemberService.py -> __name__ (MemberService) 회원관리 클래스와 메서드
# ScoreService.py -> __name__ (ScoreService) 성적관리 클래스와 메서드
# BoardService.py -> 게시판관리 클래스와 메서드
# itemService.py -> 상품관리 클래스와 메서드
# CartService.py -> 장바구니관리 클래스와 메서드

# 파이썬확장자.py로 만든 파이썬 파일은 모두 모듈로 처리 가능

def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# print(add(1,4))
# print(sub(4,2))
# 터미널에 python을 실행하고
# import를 mod1을 했더니
# 바로 print문이 실행됨
# 당연한 결과
# 근데 main에서 실행하면
# mod1.py에서 print 2개가 실행되고
# main.py에서 print 2개가 실행됨
# main에서는 add와 sub함수만 호출해서 사용하려고 함
# 이 때는 if문으로 실행을 조절해야함
if __name__ == '__main__':
    # 클래스나 모듈이 호출된 자신이 main역할인지 확인
    print(add(3,4))
    print(sub(5,3))

print(__name__) # mod1