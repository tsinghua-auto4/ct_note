import sys

input = sys.stdin.readline;


# 자릿수를 반환하는 함수
def onesPosition(n):
    ones = "1"  # 1로만 이루어진 수, 가장 작은 1부터 시작
    ans = 1  # 자릿수, 1로 초기화
    while True:
        if int(ones) % n == 0:
            ans = len(ones)  # 자릿수
            break
        ones += "1"  # 나눠 떨어지지 않으면 자릿수 계속 추가
    return ans


# 숫자 입력 받기
while True:
    try:
        n = int(input())
    except:
        break

    print(onesPosition(n))