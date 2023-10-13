from collections import deque

def fire_storm(size):
    global grid

    new_grid = [[0]*(2**N) for _ in range(2**N)]
    #행열열행 -> 공식이다 그냥 외워
    for r in range(0, 2**N, size):
        for c in range(0, 2**N, size):
            for i in range(size):
                for j in range(size):
                    new_grid[r+j][c+size-1-i] = grid[r+i][c+j]
    grid = new_grid

    melt = []
    for cr in range(2**N):
        for cc in range(2**N):
            ice = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr+dr, cc+dc
                if not (0 <= nr < 2**N and 0 <= nc < 2**N):
                    continue
                if grid[nr][nc] > 0:
                    ice += 1
            if ice < 3 and grid[cr][cc] > 0:
                melt.append([cr, cc])
    for cr, cc in melt:
        grid[cr][cc] -= 1

def counter():
    visit = [[False]*(2**N) for _ in range(2**N)]
    res   = [0, 0]

    for ir in range(2**N):
        for ic in range(2**N):
            if visit[ir][ic] or grid[ir][ic] == 0:
                continue
            area = 0
            q = deque([[ir, ic]])
            visit[ir][ic] = True
            while q:
                cr, cc =  q.popleft()
                res[0] += grid[cr][cc]
                area   += 1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = cr+dr, cc+dc
                    if not (0 <= nr < 2**N and 0 <= nc < 2**N) or visit[nr][nc]:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    visit[nr][nc] = True
                    q.append([nr, nc])
            res[1] = max(res[1], area)
    print(res[0])
    print(res[1])


N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
L    = list(map(int, input().split()))

for l in L:
    fire_storm(2**l)
counter()