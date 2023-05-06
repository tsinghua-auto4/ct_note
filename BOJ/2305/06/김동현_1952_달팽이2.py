

M, N  = map(int, input().split())
graph = [[False]*N for _ in range(M)]

move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우/하/좌/상
cr, cc = 0, 0
graph[cr][cc] = True
ans = 0
d = 0

while True:
    curve = False
    go = False
    # 4개의 방향 속에서
    for i in range(d, d+4):
        dr, dc = move[i%4]
        nr, nc = cr + dr, cc + dc
        # 만약 범위를 벗어나거나 이미 방문했다면 방향을 돌려야지
        if not(0 <= nr < M and 0 <= nc < N) or graph[nr][nc]:
            curve = True
            continue
        # 가보자구
        go = True
        graph[nr][nc] = True
        cr, cc, d = nr, nc, i%4
        break
    # 꺾고 앞으로 나갔다면 ans += 1
    if curve == True and go == True:
        ans += 1
    # 앞으로 못나갔다면 게임 끝
    if go == False:
        break
    
print(ans)