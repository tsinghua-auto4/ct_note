N = int(input())
steps = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(steps))
    exit()

dp = [0]*(N)
dp[0] = steps[0]
dp[1] = steps[0] + steps[1]
dp[2] = max(steps[0]+steps[2],steps[1]+steps[2])
for idx in range(3, N):
    dp[idx] = max(dp[idx-2] + steps[idx] , dp[idx-3] + steps[idx] + steps[idx - 1])

print(dp[N-1])