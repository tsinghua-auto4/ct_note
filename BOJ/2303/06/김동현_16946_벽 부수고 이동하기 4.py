import sys
from collections import deque

def grouping(start):
    queue = deque([start])
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        group[cx][cy] = groupNum
        for iter in range(4):
            nx, ny = cx + dx[iter], cy + dy[iter]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] or graph[nx][ny] == 1:
                continue
            visit[nx][ny] = True
            queue.append((nx, ny))
            cnt += 1
    return cnt

n, m  = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visit = [[False] * m for _ in range(n)]
group = [[0] * m for _ in range(n)]

groupNum = 1
qnt = {}
qnt[0] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n): # gruoping
    for j in range(m):
        if graph[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            w = grouping((i, j))
            qnt[groupNum] = w
            groupNum += 1

for i in range(n): # sum
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for iter in range(4):
                nx, ny = i + dx[iter], j + dy[iter]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                addList.add(group[nx][ny])
            for add in addList:
                graph[i][j] += qnt[add]
                graph[i][j] %= 10

for cur in graph:
    print("".join(map(str, cur)))