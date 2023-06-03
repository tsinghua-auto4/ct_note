

a = [""] + list(input())
b = [""] + list(input())

len_a, len_b = len(a), len(b)
dp = [['']*(len_b) for _ in range(len_a)]

for cr in range(1, len_a):
    for cc in range(1, len_b):
        if a[cr] == b[cc]:
            dp[cr][cc] = dp[cr-1][cc-1] + a[cr]
        else:
            if len(dp[cr-1][cc]) >= len(dp[cr][cc-1]):
                dp[cr][cc] = dp[cr-1][cc]
            else:
                dp[cr][cc] = dp[cr][cc-1]
print(len(dp[-1][-1]))
print(dp[-1][-1])