

N     = int(input())

graph = [[0]*101 for _ in range(101)]
move  = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 방향정의, 0: x++, 1: y--, 2: x--, 3: y++

for _ in range(N):
    c, r, d, g  = map(int, input().split())
    graph[r][c] = 1

    # 커브정의
    curve = [d]
    for _ in range(g):
        for cur in curve[::-1]:
            curve.append((cur+1)%4)
    
    # 커브생성
    for cur in curve:
        dr, dc = move[cur]
        r, c   = r+dr, c+dc
        if (0 <= r < 101 and 0 <= c < 101):
            graph[r][c] = 1
    
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            ans += 1

print(ans)