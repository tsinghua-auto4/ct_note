import sys
from collections import deque
sys.setrecursionlimit(10**6)

def islandDetect(n, data, move, x , y, label):
    if not (0 <= x < n and 0 <= y < n):
        return False

    if data[x][y] == 1:
        data[x][y] = label

        for dx, dy in move:
            cx, cy = x + dx, y + dy
            islandDetect(n, data, move, cx, cy, label)
        return True

def connectSearch(n, move, target):
    global ans
    mark  = [[-1]*n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if data[i][j] == target:
                queue.append((i,j))
                mark[i][j] = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in move:
            nx, ny = cx + dx, cy + dy
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if data[nx][ny] > 0 and data[nx][ny] != target:
                ans = min(ans, mark[cx][cy])
                return
            if data[nx][ny] == 0 and mark[nx][ny] == -1:
                mark[nx][ny] = mark[cx][cy] + 1
                queue.append((nx, ny))



if __name__ == "__main__":
    n    = int(sys.stdin.readline())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    label = 2

    ans = sys.maxsize

    for i in range(n):
        for j in range(n):
            if islandDetect(n, data, move, i, j, label):
                label += 1
    
    for i in range(2, label):
        connectSearch(n, move, i)
    
    print(ans)
