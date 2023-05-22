

N, M = map(int, input().split())
mase = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]
for r in range(1, N+1):
    for c in range(1, M+1):
        # dp와 mase의 좌표차이는 abs(1, 1)
        dp[r][c] = mase[r-1][c-1] + max(dp[r-1][c], dp[r-1][c-1], dp[r][c-1])
print(dp[N][M])