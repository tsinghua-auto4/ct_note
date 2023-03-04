import sys
from collections import deque
from copy import deepcopy

def counter():
    global n, m, data, queue
    tmp_data = deepcopy(data)
    tmp_queue = deepcopy(queue)
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    while tmp_queue:
        cx, cy = tmp_queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp_data[nx][ny] == 0:
                tmp_data[nx][ny] = 2
                tmp_queue.append((nx, ny))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 0:
                cnt += 1
    return cnt


def solution(_depth):
    global ans
    if _depth == 3:
        ans = max(ans, counter())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                solution(_depth+1)
                data[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            queue.append((i, j))

solution(0)
print(ans)