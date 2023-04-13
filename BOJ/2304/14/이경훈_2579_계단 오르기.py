import sys

input = sys.stdin.readline

N = int(input())
ans_list = []
stair = [0]
for _ in range(N):
  stair.append(int(input()))

dp = [0] * (N + 1)
dp[0] = stair[0]
dp[1] = stair[1]

if N == 1:
  print(dp[1])
else:
  dp[2] = stair[1] + stair[2]

  for i in range(3, N + 1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

  print(dp[N])
