import sys
from collections import deque

def solution():
    global n, m, k, graph

    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    
    visit = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    visit[0][0][k] = 1
    
    queue = deque([(0, 0, k)])
    while queue:
        cx, cy, w = queue.popleft()
        if cx == n - 1 and cy == m - 1:
            return visit[cx][cy][w]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w > 0 and visit[nx][ny][w-1] == 0:
                    visit[nx][ny][w-1] = visit[cx][cy][w] + 1
                    queue.append((nx, ny, w-1))
                elif graph[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[cx][cy][w] + 1
                    queue.append((nx, ny, w))
    return -1

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    graph   = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
    print(solution())