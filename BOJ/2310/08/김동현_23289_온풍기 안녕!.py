from copy import deepcopy
from collections import deque

# 로직에서 쓰일 히터 열 전파함수
def spread(x, y, heat):
    # 아직 방문처리 하지 않았다면, 방문처리/data갱신/queue추가
    if visited[x][y] == 0:
        visited[x][y] = 1
        data[x][y] += heat
        q.append([x, y])

# 히터의 방향을 정의함, 빈칸/우/좌/상/하
dx = [0, 0,  0, -1, 1]
dy = [0, 1, -1,  0, 0]

r, c, k = map(int, input().split())

# 히터 위치와 검사할 칸의 위치를 입력 받자
heater, checker = [], []
for i in range(r):
    cur = list(map(int, input().split()))
    for j in range(c):
        if 1 <= cur[j] < 5: # 온풍기가 있는 칸
            heater.append([i, j, cur[j]])
        elif cur[j] == 5: # 온도 조사가 필요한 칸
            checker.append([i, j])

# 벽에 대한 정보를 입력 받자
w = int(input())
wall = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x, y, t = map(int, input().split())
    wall[x-1][y-1].append(t)

# 칸의 정보를 담을 data와 출력인 chocolate을 선언해주자
data = [[0]*c for _ in range(r)]
chocolate = 0

# 로직을 실행해보자
while True:
    # 모든 히터들에 대해 시뮬레이션~
    for i, j, type in heater:
        q = deque()
        visited = [[0]*c for _ in range(r)]
        # 히터가 내뿜는 첫 칸의 좌표
        nx = i + dx[type]
        ny = j + dy[type]
        # 첫 칸에 열처리 추가, 히터의 바람이 나오는 방향에 있는 칸은 항상 존재함->문제 조건
        data[nx][ny] += 5

        # 만약 열을 전파할 수 있는 칸이 더 없다면, 끝낸다
        if not(0 <= nx+dx[type] < r and 0 <= ny+dy[type] < c):
            continue
        
        # 열 전파로직 시작
        q.append([nx, ny])
        flag = 0
        for num in range(4, 0, -1):
            for _ in range(len(q)):
                x, y = q.popleft()

                # 방향이 오른쪽인 히터라면
                if type == 1:
                    # 다음 전파할 칸이 범위를 벗어난다면 끝냄
                    if y+1 >= c:
                        flag = 1
                        break
                    # 전파 방향에 벽이 없다면 전파
                    if 1 not in wall[x][y]:
                        nx, ny = x, y+1
                        spread(nx, ny, num)
                    # 대각선에 열을 전파할 수 있는지 확인하고 전파
                    if x-1 >= 0:
                        if 0 not in wall[x][y] and 1 not in wall[x-1][y]:
                            nx, ny = x-1, y+1
                            spread(nx, ny, num)
                    if x+1 < r:
                        if not wall[x+1][y]:
                            nx, ny = x+1, y+1
                            spread(nx, ny, num)

                # 방향이 왼쪽인 히터라면
                elif type == 2:
                    # 다음 전파할 칸이 범위를 벗어난다면 끝냄
                    if y-1 < 0:
                        flag = 1
                        break
                    # 전파 방향에 벽이 없다면 전파
                    if 1 not in wall[x][y-1]:
                        nx, ny = x, y-1
                        spread(nx, ny, num)
                    # 대각선에 열을 전파할 수 있는지 확인하고 전파
                    if x-1 >= 0:
                        if 1 not in wall[x-1][y-1] and 0 not in wall[x][y]:
                            nx, ny = x-1, y-1
                            spread(nx, ny, num)
                    if x+1 < r:
                        if 1 not in wall[x+1][y-1] and 0 not in wall[x+1][y]:
                            nx, ny = x+1, y-1
                            spread(nx, ny, num)
                
                # 방향이 위쪽인 히터라면
                elif type == 3:
                    # 다음 전파할 칸이 범위를 벗어난다면 끝냄
                    if x-1 < 0:
                        flag = 1
                        break
                    # 전파 방향에 벽이 없다면 전파
                    if 0 not in wall[x][y]:
                        nx, ny = x-1, y
                        spread(nx, ny, num)
                    # 대각선에 열을 전파할 수 있는지 확인하고 전파
                    if y-1 >= 0:
                        if not wall[x][y-1]:
                            nx, ny = x-1, y-1
                            spread(nx, ny, num)
                    if y+1 < c:
                        if 0 not in wall[x][y+1] and 1 not in wall[x][y]:
                            nx, ny = x-1, y+1
                            spread(nx, ny, num)

                # 방향이 아래쪽인 히터라면
                elif type == 4:
                    # 다음 전파할 칸이 범위를 벗어난다면 끝냄
                    if x+1 >= r:
                        flag = 1
                        break
                    # 전파 방향에 벽이 없다면 전파
                    if 0 not in wall[x+1][y]:
                        nx, ny = x+1, y
                        spread(nx, ny, num)
                    # 대각선에 열을 전파할 수 있는지 확인하고 전파
                    if y-1 >= 0:
                        if 0 not in wall[x+1][y-1] and 1 not in wall[x][y-1]:
                            nx, ny = x+1, y-1
                            spread(nx, ny, num)
                    if y+1 < c:
                        if 1 not in wall[x][y] and 0 not in wall[x+1][y+1]:
                            nx, ny = x+1, y+1
                            spread(nx, ny, num)
                
                # 전파할 칸이 없으면 끝냄
                if flag == 1 or len(q) == 0:
                    break

    # 히터에서 나온 열들이 주변 칸에 퍼지는 로직
    tmp = deepcopy(data)
    for x in range(r):
        for y in range(c):
            direction = []
            if x < r-1 and 0 not in wall[x+1][y]:
                direction.append(4)
            if 1 not in wall[x][y]:
                direction.append(1)
            
            for d in direction:
                nx, ny = x+dx[d], y+dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if data[x][y] > data[nx][ny]:
                        diff = (data[x][y] - data[nx][ny])//4
                        tmp[x][y]   -= diff
                        tmp[nx][ny] += diff
                    elif data[x][y] < data[nx][ny]:
                        diff = (data[nx][ny] - data[x][y])//4
                        tmp[x][y]   += diff
                        tmp[nx][ny] -= diff

    # 가장자리의 칸의 온도가 1보다 높으면 1씩 뺌
    data = tmp
    for i in range(r):
        if i == 0 or i == r-1:
            for j in range(c):
                if data[i][j] > 0:
                    data[i][j] -= 1
        else:
            for j in [0, c-1]:
                if data[i][j] > 0:
                    data[i][j] -= 1
    
    # 이번 턴을 끝냈으니, 초콜릿을 추가해주자
    chocolate += 1
    if chocolate > 100:
        break

    # 확인할 칸이 모두 온도 k보다 높은지 확인
    flag = 0
    for x, y in checker:
        if data[x][y] < k:
            flag = 1
            break
    if flag == 0:
        break

print(chocolate)