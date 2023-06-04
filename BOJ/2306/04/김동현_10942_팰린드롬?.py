import sys

N       = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [[0]*N for _ in range(N)]
for iter in range(N): # 숫자 하나는 펠린드롬
    dp[iter][iter] = 1
for iter in range(N-1): # 숫자 두개가 같아도 펠린드롬
    if numbers[iter] == numbers[iter+1]:
        dp[iter][iter+1] = 1
    else:
        dp[iter][iter+1] = 0
for scale in range(N-2): # 숫자가 3개 이상일 때는 첫번째 마지막 숫자가 같고, 중간이 펠린드롬이면 펠린드롬임
    for start in range(N-2-scale):
        end = start+2+scale
        if numbers[start] == numbers[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])