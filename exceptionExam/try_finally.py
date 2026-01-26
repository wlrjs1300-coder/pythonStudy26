# try-finally : try문 수행 중, 예외 발생 여부에 상관없이 무조건 수행되는 문장

try: # 예외가 발생할 거 같은 실행문
    f = open("foo.txt","w")
    # 여러 실행문
finally: # 중간에 오류가 생기든 안생기든 실행
    f.close()