import sys
input = sys.stdin.readline;
test = map(int, input().split())

ans = 0
for n in test:
    ones = "1"      # 1로만 이루어진 수, 가장 작은 1부터 시작
    while True:
        if int(ones) % n == 0:
            ans = len(ones)
            break
        ones += "1" # 나눠 떨어지지 않으면 자릿수 계속 추가
    print(ans)
