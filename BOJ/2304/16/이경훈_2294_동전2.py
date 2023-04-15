import sys

input = sys.stdin.readline

INF = int(1e9)
n, k = map(int, input().split())
coin = [0]

for i in range(n):
    coin.append(int(input()))

# dp[C] C를 만들기 위한 사용개수

dp = [INF for _ in range(k + 1)]

dp[0] = 0
for i in range(1, n + 1):
    for j in range(coin[i], k + 1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

print(dp[k]) if dp[k] != INF else print(-1)