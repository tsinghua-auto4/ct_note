import copy

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while tmp[x][y]:
                d = tmp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    global max_eat, shark, eat
    if dep == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(tmp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)


# 물고기 이동 방향
f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 상어 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 기본 입력
m, s  = map(int, input().split())
fish  = [list(map(int, input().split())) for _ in range(m)]
shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0]*4 for _ in range(4)]

# 그래프 선언
graph = [[[] for _ in range(4)] for _ in range(4)]

# 그래프에 저장하는 물고기는 방향 데이터 형식으로 저장함
for x, y, d in fish:
    graph[x-1][y-1].append(d-1)

# 로직 시작
for _ in range(s):
    eat = list() # 이번 턴에 상어가 이동한 칸
    max_eat = -1 # 최대로 먹은 물고기 수

    # 1. 물고기 복제
    tmp = copy.deepcopy(graph)
    # 2. 물고기 이동
    tmp = move_fish()
    # 3. 상어이동
    dfs(shark[0], shark[1], 0, 0, list())
    for x, y in eat:
        if tmp[x][y]:
            tmp[x][y]   = []
            smell[x][y] = 3
    # 4. 냄새 처리
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 5. 복제마법 실행
    for i in range(4):
        for j in range(4):
            graph[i][j] += tmp[i][j]

# 물고기 수 구하기
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(graph[i][j])

print(ans)