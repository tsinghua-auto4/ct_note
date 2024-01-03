N, M = map(int, input().split())
mem = dict()
for _ in range(N):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if (r, c) not in mem.keys():
                mem[(r, c)] = 1
            else:
                mem[(r, c)] += 1

ans = 0
for cur in mem.values():
    if cur > M:
        ans += 1
print(ans)