
N, M = map(int, input().split())
S = {}
for _ in range(N):
    S[str(input())] = 0

ans = 0
for _ in range(M):
    cur = str(input())
    if cur in S:
        ans += 1

print(ans)