import copy

def teen_shark(sr, sc, score, grid):
    global move, ans

    # 상어이동, 백트래킹-1
    score += grid[sr][sc][0]
    ans = max(ans, score)
    grid[sr][sc][0] = 0

    # 물고기 이동
    for f in range(1, 17):
        fr, fc, fd = -1, -1, -1 # 물고기 위치 & 방향
        for r in range(4):
            for c in range(4):
                if grid[r][c][0] == f:
                    fr, fc= r, c
                    break
        if fr == -1 and fc == -1:
            continue

        fd = grid[fr][fc][1]

        for i in range(8):
            nd = (fd+i)%8
            dr, dc = move[nd]
            nr, nc = fr+dr, fc+dc
            # 물고기가 갈 칸이 그리드를 벗어나거나, 상어의 위치와 같다면 다음 방향을 탐색함
            if not (0 <= nr < 4 and 0 <= nc < 4) or (nr==sr and nc==sc):
                continue
            # 조건에 맞다면 방향을 갱신해주고 물고기 위치를 교환하자
            grid[fr][fc][1] = nd
            grid[fr][fc], grid[nr][nc] = grid[nr][nc], grid[fr][fc]
            break
    
    # 상어이동, 백트래킹-2
    sd = grid[sr][sc][1]
    for depth in range(1, 5):
        dr, dc = move[sd]
        nr, nc = sr+dr*depth, sc+dc*depth
        if (0 <= nr < 4 and 0 <= nc < 4) and grid[nr][nc][0] > 0:
            teen_shark(nr, nc, score, copy.deepcopy(grid))


move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
grid = []
for _ in range(4):
    data = list(map(int, input().split()))
    row  = []
    for idx in range(0, 8, 2):
        row.append([data[idx], data[idx+1]-1])
    grid.append(row)

ans = 0
teen_shark(0, 0, 0, grid)
print(ans)