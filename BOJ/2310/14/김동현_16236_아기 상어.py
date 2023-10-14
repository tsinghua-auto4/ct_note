from collections import deque
import heapq

def baby_shark(r, c):
    global N, shark_posi, shark_stat, grid

    move  = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    cand  = []

    q     = deque([[r, c]])
    visit = [[0]*N for _ in range(N)]
    visit[r][c] = 1
    
    while q:
        cr, cc = q.popleft()

        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not(0 <= nr < N and 0 <= nc < N) or visit[nr][nc] != 0:
                continue
            
            # Case1. 물고기가 있고, 상어의 크기보다 작아서 먹을 수 있음
            if grid[nr][nc] < grid[r][c] and grid[nr][nc] != 0:
                visit[nr][nc] = visit[cr][cc]+1
                heapq.heappush(cand, (visit[nr][nc]-1, nr, nc))

            # Case2. 물고기가 있고, 상어의 크기보다 커서 먹을 수 없음
            elif grid[nr][nc] == grid[r][c]:
                visit[nr][nc] = visit[cr][cc]+1
                q.append([nr, nc])

            # Case3. 물고기가 없고, step만 늘음
            elif grid[nr][nc] == 0:
                visit[nr][nc] = visit[cr][cc]+1
                q.append([nr, nc])
    
    return cand


N     = int(input())
shark_stat = [2, 0]   # 크기, 먹은 물고기 수
shark_posi = [-1, -1] # 위치

grid = []
for r in range(N):
    cur = list(map(int, input().split()))
    grid.append(cur)

    if shark_posi == [-1, -1]:
        for c in range(N):
            if cur[c] == 9:
                shark_posi = [r, c]

time = 0
sr, sc = shark_posi
while True:
    grid[sr][sc] = shark_stat[0]
    cand = baby_shark(sr, sc)

    if len(cand) == 0:
        break

    step, nr, nc = cand[0]
    time += step
    shark_stat[1] += 1

    if shark_stat[0] == shark_stat[1]:
        shark_stat[0] += 1
        shark_stat[1] = 0
    
    grid[sr][sc] = 0
    sr, sc = nr, nc

print(time)