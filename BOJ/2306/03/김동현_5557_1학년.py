

N       = int(input())
numbers = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(N)]
dp[0][numbers[0]] = 1

for cr in range(1, N-1):
    for cc in range(21):
        if dp[cr-1][cc]:
            if 0 <= cc + numbers[cr] <= 20:
                dp[cr][cc+numbers[cr]] += dp[cr-1][cc]
            if 0 <= cc - numbers[cr] <= 20:
                dp[cr][cc-numbers[cr]] += dp[cr-1][cc]
print(dp[N-2][numbers[-1]])