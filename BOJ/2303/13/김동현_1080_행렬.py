import sys

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]

n, m = map(int, sys.stdin.readline().split())
a    = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
b    = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            reverse(i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit()
print(cnt)