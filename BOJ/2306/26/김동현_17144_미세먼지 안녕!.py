

def diffusion(R: int, C: int, target:list[list], purifier: list):
    graph = [[0]*C for _ in range(R)]
    graph[purifier[0][0]][purifier[0][1]] = -1
    graph[purifier[1][0]][purifier[1][1]] = -1
    
    for cr in range(R):
        for cc in range(C):
            if target[cr][cc] <= 0:
                continue
            diffuse = target[cr][cc]//5
            grid    = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr+dr, cc+dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if (nr, nc) in purifier:
                    continue
                graph[nr][nc] += diffuse
                grid += 1
            graph[cr][cc] += (target[cr][cc] - diffuse*grid)
    for r in range(R):
        for c in range(C):
            target[r][c] = graph[r][c]


def purify(R: int, C: int, target:list[list], purifier: list):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    # 위쪽 반시계 방향 기류
    direction = 1
    past = 0
    cr, cc = purifier[0][0], 1
    while True:
        nr, nc = cr+dr[direction], cc+dc[direction]
        if nr == R or nc == C or nr == -1 or nc == -1:
            direction = (direction-1)%4
            continue
        if cr == purifier[0][0] and cc == 0:
            break
        target[cr][cc], past  = past, target[cr][cc]
        cr, cc = nr, nc

    # 아래쪽 시계방향 기류
    direction = 1
    past = 0
    cr, cc = purifier[1][0], 1
    while True:
        nr, nc = cr+dr[direction], cc+dc[direction]
        if nr == R or nc == C or nr == -1 or nc == -1:
            direction = (direction+1)%4
            continue
        if cr == purifier[1][0] and cc == 0:
            break
        target[cr][cc], past  = past, target[cr][cc]
        cr, cc = nr, nc


def solution(R: int, C: int, T: int, target:list[list], purifier: list):
    # T번 반복
    for _ in range(T):
        # 1. 먼지 확산
        diffusion(R, C, target, purifier)
        # 2. 공기 청정기 동작
        purify(R, C, target, purifier)

    # 미세먼지의 양 계산
    ans = 2
    for idx in range(R):
        ans += sum(target[idx])

    return ans


R, C, T  = map(int, input().split())
graph    = [] # 필드 기억
purifier = [] # 공기 청정기 위치
for r in range(R):
    cur = list(map(int, input().split()))
    graph.append(cur)
    for c in range(C):
        if cur[c] == -1:
            purifier.append((r, c))

print(solution(R, C, T, graph, purifier))