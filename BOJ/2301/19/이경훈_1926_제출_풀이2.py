import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#입력
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북
ans = 0

# dfs 함수
def dfs(x, y):
    global cnt
    cnt += 1
    data[x][y] = 0
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if -1 < nx < n and -1 < ny < m:
            if data[nx][ny] == 1:
                dfs(nx, ny)
  

num = 0
ans = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            cnt = 0
            dfs(i, j)
            num += 1
            if cnt > ans:
                ans = cnt

print(num)
print(ans)