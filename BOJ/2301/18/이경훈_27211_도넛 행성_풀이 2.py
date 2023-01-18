import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = True    
    for i in range(4):
        nx = (x + dx[i]) % n # n*m 격자를 넘어가도 그 반대로 가게 함
        ny = (y + dy[i]) % m
        if data[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)
            

ans = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            ans += 1
print(ans)