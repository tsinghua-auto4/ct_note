
def update_smell():
    global N, M, K, grid

    for r in range(N):
        for c in range(N):
            if smell[r][c][1] > 0: # 냄새가 남아있다면 -1 해주고
                smell[r][c][1] -= 1
            if grid[r][c] != 0:   # 현재 칸에 상어가 있다면 냄새를 추가해주자
                smell[r][c] = [grid[r][c], K]

def adult_shark():
    global N, M, K, grid

    ngrid = [[0]*N for _ in range(N)]
    for cr in range(N):
        for cc in range(N):
            if grid[cr][cc] != 0: # 상어가 있다면 이동
                cd    = shark_dir[grid[cr][cc]]
                found = False

                for dir in shark_prio[grid[cr][cc]][cd]:
                    dr, dc = move[dir]
                    nr, nc = cr+dr, cc+dc
                    if not(0 <= nr < N and 0 <= nc < N):
                        continue
                    if smell[nr][nc][1] == 0:
                        shark_dir[grid[cr][cc]] = dir

                        if ngrid[nr][nc] == 0:
                            ngrid[nr][nc] = grid[cr][cc]
                        else:
                            ngrid[nr][nc] = min(grid[cr][cc], ngrid[nr][nc])
                        
                        found = True
                        break
                if found:
                    continue

                for dir in shark_prio[grid[cr][cc]][cd]:
                    dr, dc = move[dir]
                    nr, nc = cr+dr, cc+dc
                    if not(0 <= nr < N and 0 <= nc < N):
                        continue
                    if smell[nr][nc][0] == grid[cr][cc]:
                        shark_dir[grid[cr][cc]] = dir
                        ngrid[nr][nc] = grid[cr][cc]
                        break
    return ngrid


N, M, K = map(int, input().split())
grid    = [list(map(int, input().split())) for _ in range(N)]

move    = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

shark_dir = {}
tmp = list(map(int, input().split()))
for idx in range(1, M+1):
    shark_dir[idx] = tmp[idx-1]

shark_prio = {}
for idx in range(1, M+1):
    shark_prio[idx] = {}
    for iter in range(1, 4+1):
        shark_prio[idx][iter] = list(map(int, input().split()))

smell = [[[0, 0]]*N for _ in range(N)]

ans = 0
while True:
    update_smell()
    grid = adult_shark()
    ans += 1

    check = True
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 1:
                check = False
                break
    
    if check:
        print(ans)
        break

    if ans >= 1000:
        print(-1)
        break