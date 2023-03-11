import sys
from collections import deque

def solution(x, y, visit):
    queue = deque([(x, y)])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if space[nx][ny] == space[cx][cy]:
                    visit[nx][ny] = visit[cx][cy]
                    queue.append((nx, ny))

n     = int(sys.stdin.readline().rstrip())
space = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

ans   = []

cnt = 0
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            solution(i, j, visit)
            cnt += 1
ans.append(cnt)

for i in range(n):
    for j in range(n):
        if space[i][j] == 'G':
            space[i][j] = 'R'
cnt = 0
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            solution(i, j, visit)
            cnt += 1
ans.append(cnt)

print(*ans)