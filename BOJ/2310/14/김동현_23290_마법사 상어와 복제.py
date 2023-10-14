import copy

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            while tmp[r][c]:
                d = tmp[r][c].pop()
                for i in range(d, d-8 , -1):
                    i %= 8
                    dr, dc = dir_fish[i]
                    nr, nc = r+dr, c+dc
                    if (nr, nc) != shark and (0 <= nr < 4 and 0 <= nc < 4) and not smell[nr][nc]:
                        res[nr][nc].append(i)
                        break
                else:
                    res[r][c].append(d)
    return res

def move_shark(sr, sc, depth, cnt, visit):
    global eat, shark, max_eat

    if depth == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (sr, sc)
            eat = visit[:]
        return
    for d in range(4):
        dr, dc = dir_shark[d]
        nr, nc = sr+dr, sc+dc
        if not(0 <= nr < 4 and 0 <= nc < 4):
            continue
        if (nr, nc) not in visit:
            visit.append((nr, nc))
            move_shark(nr, nc, depth+1, cnt+len(tmp[nr][nc]), visit)
            visit.pop()
        else:
            move_shark(nr, nc, depth+1, cnt, visit)


dir_shark = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir_fish  = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

M, S  = map(int, input().split())
fish  = [list(map(int, input().split())) for _ in range(M)]
shark = tuple(map(lambda x: int(x)-1, input().split()))
smell = [[0]*4 for _ in range(4)]

grid  = [[[] for _ in range(4)] for _ in range(4)]

for r, c, d, in fish:
    grid[r-1][c-1].append(d-1)

for _ in range(S):
    eat = list() # 이번 턴에서 상어가 먹은 물고기의 좌표 list
    max_eat = -1 # 이번 턴에서 상어가 먹은 물고기의 수
    # 물고기 복제 & 이동
    tmp = copy.deepcopy(grid)
    tmp = move_fish()
    # 상어이동
    move_shark(shark[0], shark[1], 0, 0, list())
    for r, c in eat:
        if tmp[r][c]:
            tmp[r][c] = []
            smell[r][c] = 3
    # 냄새처리
    for r in range(4):
        for c in range(4):
            if smell[r][c]:
                smell[r][c] -= 1
    # 복제마법
    for r in range(4):
        for c in range(4):
            grid[r][c] += tmp[r][c]

ans = 0
for r in range(4):
    for c in range(4):
        ans += len(grid[r][c])
print(ans)