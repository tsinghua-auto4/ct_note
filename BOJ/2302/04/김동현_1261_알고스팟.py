import sys
from collections import deque

def solution(n, m, wall, visited):
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if (x+1, y+1) == (n, m):
            return visited[x][y]

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x+dx, y+dy
            if (0<= nx < n and 0<= ny < m) and visited[nx][ny] == -1:
                if wall[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    wall[nx][ny] = 0
                else:
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]



if __name__ == "__main__":
    m, n    = map(int, sys.stdin.readline().split())
    wall    = [[] for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 0

    for i in range(n):
        wall[i] = list(map(int, sys.stdin.readline().rstrip()))

    print(solution(n, m, wall, visited))