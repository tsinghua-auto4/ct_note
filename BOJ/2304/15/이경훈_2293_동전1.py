import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0]

for i in range(n):
    coin.append(int(input()))

# dp[i] i원이 되는 경우의 수

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in range(1, n+1):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])