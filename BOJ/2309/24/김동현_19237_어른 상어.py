n, m, k = map(int, input().split())

# 상어의 초기 위치
data = [list(map(int, input().split())) for _ in range(n)]

# 상어의 초기방향 설정
directions = list(map(int, input().split()))

# 상어의 상황별 우선순위
priorities = []
for i in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(int, input().split())))
    priorities.append(tmp)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 상황판 그리기(상어의 번호/냄새 남은 시간/방향)
smell = [[[0, 0]] * n for _ in range(n)]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]

# 상어 이동
def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                direction = directions[data[x][y] - 1]
                found = False
                # 상어의 위치인 경우
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dr[idx - 1]
                    ny = y + dc[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면 갈 수 있음
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else:
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue

                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dr[idx - 1]
                    ny = y + dc[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y]: # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

ans = 0
while True:
    update_smell()
    new_data = move()
    data = new_data
    ans += 1

    check = True
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
                break
    
    if check:
        print(ans)
        break

    if ans >= 1000:
        print(-1)
        break