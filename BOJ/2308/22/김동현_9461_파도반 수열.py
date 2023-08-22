
dp = [1]*101
for iter in range(4, 101):
    dp[iter] = dp[iter-2] + dp[iter-3]

T = int(input())
for _ in range(T):
    target = int(input())
    print(dp[target])