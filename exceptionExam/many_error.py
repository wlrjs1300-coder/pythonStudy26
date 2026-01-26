# 여러가지의 오류들이 발생한다면
# try 문 안에서 여러개의 오류 처리

try:
    4 / 0
    a = [1,2]
    print(a[3])
# except ZeroDivisionError as e:
#     print(e)
#     print("0으로 나눠지는 예외 발생")
# except IndexError as e:
#     print(e)
#     print("리스트 인덱스 범위 초과")

except(ZeroDivisionError, IndexError) as e:
    print(e)
    print("0으로 나눴거나 리스트의 범위 초과 예외 발생")
    print("예외 발생 시, 담당자에게 문의하세요 : 전화번호")