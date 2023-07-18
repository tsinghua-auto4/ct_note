N, K = map(int, input().split())

dp = [[1 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, K+1):
    for j in range(i+1, N+1):
        dp[j][i] = (dp[j-1][i-1] + dp[j-1][i])

print(dp[N][K])