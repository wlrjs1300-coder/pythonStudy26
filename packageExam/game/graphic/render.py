# 만약 이 곳에서 sound 디렉토리에 있는 echo.py 모듈을 사용하고 싶다면

from ..sound.echo import echo_test
#    .. : 상위폴더로 이동 -> game

def render_test():
    print("render_test")
    print("graphic/render_test.py를 실행")
    echo_test()