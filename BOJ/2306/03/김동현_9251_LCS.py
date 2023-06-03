

a, b = input(), input()

len_r, len_c = len(a), len(b)
dp = [[0]*(len_c+1) for _ in range(len_r+1)]

for cr in range(1, len_r+1):
    for cc in range(1, len_c+1):
        if a[cr-1] == b[cc-1]:
            dp[cr][cc] = dp[cr-1][cc-1] + 1
        else:
            dp[cr][cc] = max(dp[cr][cc-1], dp[cr-1][cc])
print(dp[-1][-1])