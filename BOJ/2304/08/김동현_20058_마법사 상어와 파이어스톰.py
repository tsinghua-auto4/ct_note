import sys
from collections import deque

def fire_storm(size):
    global N, Q, grid

    # size 별로 회전
    new_grid = [[0]*(2**N) for _ in range(2**N)]
    for y in range(0, 2**N, size): # 격자 시작 좌표 y축
        for x in range(0, 2**N, size): # 격자 시작 좌표 x축
            for i in range(size): # 열 인덱스
                for j in range(size): # 행 인덱스
                    new_grid[y + j][x + size - i - 1] = grid[y + i][x + j]

    grid = new_grid
    # 모든 그리드의 상하좌우에 얼음이 3칸이상 없으면 얼음 -1, 얼음은 한번에 같이 녹음
    melt_list = []
    for i in range(2**N):
        for j in range(2**N):
            ice_cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i+dx, j+dy
                if not (0 <= nx < 2**N and 0 <= ny < 2**N):
                    continue
                if grid[nx][ny] > 0:
                    ice_cnt += 1
            if ice_cnt < 3 and grid[i][j] > 0:
                melt_list.append((i, j))
    for x, y in melt_list:
        grid[x][y] -= 1

def counter():
    global N, grid
    visit = [[False]*(2**N) for _ in range(2**N)]
    res   = [0, 0]
    for x in range(2**N):
        for y in range(2**N):
            area_cnt = 0
            if visit[x][y] or grid[x][y] == 0:
                continue
            queue = deque([(x, y)])
            visit[x][y] = True
            while queue:
                cx, cy = queue.popleft()
                res[0] += grid[cx][cy]
                area_cnt += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx+dx, cy+dy
                    if not (0 <= nx < 2**N and 0 <= ny < 2**N) or visit[nx][ny]:
                        continue
                    if grid[nx][ny] != 0:
                        visit[nx][ny] = True
                        queue.append((nx, ny))
            res[1] = max(res[1], area_cnt)
    
    print(res[0])
    print(res[1])


N, Q = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(2**N)]
L    = list(map(int, sys.stdin.readline().split()))

for cur in L:
    fire_storm(2**cur)
counter()