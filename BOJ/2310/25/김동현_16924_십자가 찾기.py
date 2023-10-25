move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def checks(y, x):
    for s in range(1, M):
        flag = True
        for i in range(4):
            dy, dx = move[i]
            ny, nx = y + dy*s, x + dx*s
            if 0 <= nx < M and 0 <= ny < N and mat[ny][nx] == '*':
                pass
            else:
                # exit
                flag = False
                break
        if flag:
            ans.append([y + 1, x + 1, s])
            for i in range(4):
                dy, dx = move[i]
                ny, nx = y + dy*s, x + dx*s
                check[ny][nx] = 0
            check[y][x] = 0
        else:
            break

N, M  = map(int, input().split())
check = [[0]*M for _ in range(N)]

mat = []
ans = []

total = 0
for i in range(N):
    mat.append(input())
    for j in range(M):
        if mat[i][j] == '*':
            check[i][j] = 1

for i in range(N):
    for j in range(M):
        if mat[i][j] == '*':
            checks(i, j)


for i in range(N):
    for j in range(M):
        total += check[i][j]

if total == 0:
    print(len(ans))
    for ss in ans:
        print(*ss)
else:
    print(-1)