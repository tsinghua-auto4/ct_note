from collections import deque

N, M = map(int, input().split())
grid = []

sr, sc = -1, -1
for r in range(N):
    cur = list(map(str, input()))
    for c in range(M):
        if cur[c] == 'I':
            sr, sc = r, c
    grid.append(cur)

ans   = 0
visit = [[0]*M for _ in range(N)]
visit[sr][sc] == 1

q = deque([[sr, sc]])
while q:
    cr, cc = q.popleft()
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = cr+dr, cc+dc
        if not(0 <= nr < N and 0 <= nc < M) or visit[nr][nc] > 0:
            continue

        if grid[nr][nc] == 'X':
            continue
        elif grid[nr][nc] == 'O':
            visit[nr][nc] = 1
            q.append([nr,nc])
        elif grid[nr][nc] == 'P':
            visit[nr][nc] = 1
            q.append([nr,nc])
            ans += 1

if ans > 0:
    print(ans)
else:
    print("TT")