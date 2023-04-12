n, k  = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp    = [10001]*(k+1)
dp[0] = 0
for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] = min(dp[j-i]+1, dp[j])
if dp[k] == 10001:
    print(-1)
    exit()
print(dp[k])