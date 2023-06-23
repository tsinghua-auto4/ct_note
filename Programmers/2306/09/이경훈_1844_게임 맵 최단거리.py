from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n, m = -1, -1

def inside(r, c):
    return -1 < r < n and -1 < c < m
    
def solution(maps):
    global n, m
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        if r == n-1 and c == m-1:
            break
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not inside(nr, nc):
                continue
            if maps[nr][nc] == 0 or visited[nr][nc] != 0:
                continue
            q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
    if visited[n-1][m-1] != 0:
        answer = visited[n-1][m-1]
    else:
        answer = -1
    
    return answer