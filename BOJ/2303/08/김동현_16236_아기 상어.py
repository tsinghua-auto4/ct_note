import sys
from collections import deque

def solution(x, y):
    visit = [[0]*n for _ in range(n)]
    queue = deque([(x, y)])
    cand  = []
    move  = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    visit[x][y] = 1

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in move:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[x][y] > graph[nx][ny] and graph[nx][ny] != 0:
                    visit[nx][ny] = visit[cx][cy] + 1
                    cand.append((visit[nx][ny] - 1, nx, ny))
                elif graph[x][y] == graph[nx][ny]:
                    visit[nx][ny] = visit[cx][cy] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visit[nx][ny] = visit[cx][cy] + 1
                    queue.append((nx, ny))
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))

n     = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

shark_pos = []
for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                shark_pos.append(i)
                shark_pos.append(j)
                break

cnt = 0
i, j = shark_pos
size = [2, 0]
while True:
    graph[i][j] = size[0]
    cand = deque(solution(i,j))
    
    if not cand:
        break
        
    step, nx, ny = cand.popleft()
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[i][j] = 0
    i, j = nx, ny
        
print(cnt)