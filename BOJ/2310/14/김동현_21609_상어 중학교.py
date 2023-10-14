import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def rotate(graph):
    global n, m, grid
    new_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_grid[i][j] = graph[j][n-1-i]

    grid = new_grid
    return

def gravity(graph):
    global n, m, grid
    for j in range(n):
        for i in range(n-1, -1, -1):
            if graph[i][j] >= 0:
                for k in range(i+1, n+1):
                    if k == n or graph[k][j] >= -1:
                        graph[i][j], graph[k-1][j] = graph[k-1][j], graph[i][j]
                        break

#최대 크기 블록 찾기
def grouping(graph):
    max_block = [[0, 0]]
    max_count = 0
    max_rainbow_count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            #아직 처리 안한 일반 블록이 아니면 컨티뉴
            if graph[i][j] <= 0 or visited[i][j]:
                continue

            visited[i][j] = True
            now_num = graph[i][j]

            #블록그룹 만들기
            block = [[i, j]]
            count = 0
            rainbow_count = 0

            for x, y in block:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if not(0 <= nx < n and 0 <= ny < n):
                        continue

                    #기준블록과 같은 블록그룹이면 방문처리, 블록그룹 묶기
                    if graph[nx][ny] == now_num and not visited[nx][ny]:
                        block.append([nx, ny])
                        visited[nx][ny] = True
                        count += 1

                    #무지개 블록인경우 지금 블록 그룹에 없으면 추가
                    elif graph[nx][ny] == 0 and [nx,ny] not in block:
                        block.append([nx, ny])
                        visited[nx][ny] = True
                        count += 1
                        rainbow_count += 1

            #최대 블록 크기일시 갱신
            if count > max_count:
                max_block = block
                max_count = count
                max_rainbow_count = rainbow_count

            #같은 크기일시 무지개 블록 개수로 갱신
            #크기가 같고 무지개 블록이 같은경우 나중에 탐색된 블록 그룹이 우선이므로 갱신
            elif count == max_count:
                if rainbow_count >= max_rainbow_count:
                    max_block = block
                    max_count = count
                    max_rainbow_count = rainbow_count

    if len(max_block) == 1:
        return None

    return max_block


reward = 0
while True:
    group = grouping(grid)

    if group == None:
        break

    reward += len(group) ** 2
    for x, y in group:
        grid[x][y] = -2

    gravity(grid)
    rotate(grid)
    gravity(grid)

print(reward)