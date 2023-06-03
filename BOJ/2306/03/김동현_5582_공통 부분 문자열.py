

a = [''] + list(input())
b = [''] + list(input())

len_r, len_c = len(a), len(b)
dp = [[0]*len_c for _ in range(len_r)]

ans = 0
for cr in range(1, len_r):
    for cc in range(1, len_c):
        if a[cr] == b[cc]:
            dp[cr][cc] = dp[cr-1][cc-1] + 1
            ans = max(ans, dp[cr][cc])

print(ans)