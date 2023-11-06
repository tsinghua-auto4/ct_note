N, M, K = map(int, input().split())

cur = 0
for r in range(N):
    for c in range(M):
        if cur == K:
            print(r, c)
            exit()
        cur += 1