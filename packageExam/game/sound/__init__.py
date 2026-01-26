# __all__ 내장 변수

# __init__.py 파일이 있는 상태에서
# from game.sound import * (sound 아래 모든 것)
#           패키지
# echo.echo_test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined
# echo 라는 이름이 정의되지 않았다라는 오류
# *을 사용하기 위한 방법 2가지
# 1. __init__.py 파일을 만들지 말 것 (패키지가 아님)
# 2. __init__.py 파일 안에 __all__을 이용해 제공할 것

__all__ = ["echo"] # 변수에 리스트화하여 모듈을 넣는다
#           echo.py
# __all__이 의미하는 것은 sound 패키지 하위 모듈을 import할 목록

# 이 때 착각하기 쉬운 것
# from game.sound.echo import * 은 __all__에 상관없이 import 됨
#                 마지막이 모듈이라
# from game.sound import * 는 패키지를 *로 import해서 __init__.py에 영향을 받음
#           마지막이 패키지라

