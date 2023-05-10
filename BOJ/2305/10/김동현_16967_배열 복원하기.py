

H, W, X, Y  = map(int, input().split())
graph       = [list(map(int, input().split())) for _ in range(H+X)]

ans = []

for r in range(H):
    ans.append(graph[r][:W])

for r in range(H):
    for c in range(W):
        if r+X < H and c+Y < W:
            ans[r+X][c+Y] -= ans[r][c]

for r in ans:
    print(*r)