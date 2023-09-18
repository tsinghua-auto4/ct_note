import copy

def teenshark(cr, cc, score, graph):
    global move, ans
    score += graph[cr][cc][0]
    ans = max(ans, score)
    graph[cr][cc][0] = 0

    # 물고기 이동
    for f in range(1, 17):
        # 물고기 찾기
        fr, fc = -1, -1
        for r in range(4):
            for c in range(4):
                if graph[r][c][0] == f:
                    fr, fc = r, c
                    break
        # 없으면 넘어가
        if fr == -1 and fc == -1:
            continue
        # 물고기 이동 방향
        fd = graph[fr][fc][1]

        # 물고기가 이동하려는 방향 경우의 수를 조회해보자
        for i in range(8):
            #i가 늘어날 때 마다 반시계 방향으로 회전함
            nd = (fd+i)%8
            nr, nc = fr + move[nd][0], fc + move[nd][1]
            # graph 범위를 벗어나거나 상어의 위치(cr, cc)와 같다면 다음 방향을 찾자
            if not(0 <= nr < 4 and 0 <= nc < 4) or (nr == cr and nc == cc):
                continue
            # 찾았다면 물고기 맞교환~
            graph[fr][fc][1] = nd
            graph[fr][fc], graph[nr][nc] = graph[nr][nc], graph[fr][fc]
            break
    
    # 상어이동
    sd = graph[cr][cc][1]
    # 4개의 칸이라서 이동 범위가 4까지임
    for moving in range(1, 5):
        nr, nc = cr+move[sd][0]*moving, cc+move[sd][1]*moving
        # 새로 가려는 위치가 graph범위 안에 있고, 물고기가 있다면 dfs로 max 값을 찾으러 떠나자
        if (0 <= nr < 4 and 0 <= nc < 4) and graph[nr][nc][0] > 0:
            teenshark(nr, nc, score, copy.deepcopy(graph))


move  = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
graph = [[] for _ in range(4)]

for idx in range(4):
    data = list(map(int, input().split()))
    fish = []
    for iter in range(0, 8, 2):
        fish.append([data[iter], data[iter+1]-1])
    graph[idx] = fish

ans = 0
teenshark(0, 0, 0, graph)
print(ans)