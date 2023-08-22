N = int(input())
dp = [1]*(N+1)

for idx in range(2, N+1):
    dp[idx] = (dp[idx-1] + dp[idx-2])%15746
print(dp[N])