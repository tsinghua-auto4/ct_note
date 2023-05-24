

dp = [1 for _ in range(10000+1)]
for i in range(2, 10000+1):
    dp[i] += dp[i-2]
for i in range(3, 10000+1):
    dp[i] += dp[i-3]


for _ in range(int(input())):
    N = int(input())
    print(dp[N])