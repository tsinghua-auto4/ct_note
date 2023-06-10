from itertools import combinations

N, M = map(int, input().split())
forb = [[False]*N for _ in range(N)]
for i in range(M):
    i1, i2 = map(int, input().split())
    forb[i1 - 1][i2 - 1] = True
    forb[i2 - 1][i1 - 1] = True

ans = 0
for cur in combinations(range(N), 3):
    a, b, c = cur
    if forb[a][b] or forb[b][c] or forb[a][c]:
        continue
    ans += 1
print(ans)