import sys
from collections import deque

def solution(start):
    visit       = [[k + 1 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 0

    move = ((1, 0), (-1, 0), (0, 1), (0, -1))

    queue = deque()
    queue.append(start)

    ans = 1
    day = True

    while queue:
        for _ in range(len(queue)):
            cx, cy, w = queue.popleft()
            
            if cx == n - 1 and cy == m - 1:
                return ans
            
            for dy, dx in move:
                nx, ny = cx + dy, cy + dx
                if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] <= w:
                    continue
                if graph[nx][ny] == '0':
                        visit[nx][ny] = w
                        queue.append((nx, ny, w))
                elif w < k:
                    if not day:
                        queue.append((cx, cy, w))
                    else:
                        visit[nx][ny] = w + 1
                        queue.append((nx, ny, w + 1))
        ans += 1
        day = not day
    return -1


n, m, k = map(int, sys.stdin.readline().split())
graph   = [sys.stdin.readline().rstrip() for _ in range(n)]

print(solution((0,0,0)))