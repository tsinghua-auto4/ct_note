
# 로봇청소기의 현재 위치를 입력값으로 주면 됨
def robotic_vacuum(r: int, c: int, d: int):
    global N, M, graph, ans

    turn_qcc = [3, 0, 1, 2] # turn quarter of counter clock-wise

    move_f   = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 0, 동 1, 남 2, 서 3 // 앞으로 움직임
    move_b   = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 북 0, 동 1, 남 2, 서 3 // 뒤로 움직임

    around   = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 주변을 확인하는 상대좌표

    cur = (r, c, d)
    while True:
        cr, cc, cd = cur

        # 1. 현재 칸이 벽이 아니면 청소한다.
        if graph[cr][cc] == 0:
            ans += 1
            graph[cr][cc] = -1

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
        dirty = False
        for dr, dc in around:
            nr, nc = cr+dr, cc+dc
            if (0 <= nr < N and 0 <= nc < M) and graph[nr][nc] == 0:
                dirty = True
                break

        # 주변에 더러운 칸이 있다면
        if dirty:
            nd = turn_qcc[cd] # 90도로 꺾고
            dlr, dlc = move_f[nd] # 새로운 방향에서 바라본 위치
            look_r, look_c = cr+dlr, cc+dlc
            # 갈 수 있는 칸이라면 앞으로 가자
            if (0 <= look_r < N and 0 <= look_c < M) and graph[look_r][look_c] == 0:
                cur = (look_r, look_c, nd)
            else:
                cur = (cr, cc, nd)
        
        # 주변에 더러운 칸이 없다면
        if not dirty:
            # 현재 방향의 뒤칸 확인
            dr, dc = move_b[cd]
            nr, nc = cr+dr, cc+dc
            # 만약 뒤로 움직일 수 없다면(벽이라서), 작동을 멈추자
            if not (0 <= nr < N and 0 <= nc < M) or graph[nr][nc] == 1:
                return ans
            # 뒤로 움직일 수 있다면 방향을 유지하고 뒤로
            elif (0 <= nr < N and 0 <= nc < M) and graph[nr][nc] != 1:
                cur = (nr, nc, cd)



N, M       = map(int, input().split())
ir, ic, id = map(int, input().split()) # 청소기의 현재 위치와 뱡향,  //동 0, 북 1, 남 2, 서 3
graph      = [list(map(int, input().split())) for _ in range(N)]

ans = 0
print(robotic_vacuum(ir, ic, id))