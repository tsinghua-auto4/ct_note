from itertools import combinations

N, M = map(int, input().split())
grid = []

house = []
store = []

ans = float('inf')

for r in range(N):
    cur = list(map(int, input().split()))
    for c in range(N):
        if cur[c] == 1:
            house.append([r, c])
        elif cur[c] == 2:
            store.append([r, c])

for cur in combinations(store, M):
    tmp = 0
    for h in house:
        length = float('inf')
        for chicken in range(M):
            length = min(length, abs(h[0]-cur[chicken][0])+abs(h[1]-cur[chicken][1]))
        tmp += length
    ans = min(ans, tmp)

print(ans)