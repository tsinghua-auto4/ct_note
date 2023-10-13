import sys; input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    past_clouds = []
    # 1/2/3. 모든 구름이 이동, grid 경계 없음, 구름 칸에 비가 내리고 사라짐
    while clouds:
        cr, cc = clouds.pop()
        dr, dc = move[d]
        nr, nc = (cr+dr*s)%N, (cc+dc*s)%N
        grid[nr][nc] += 1
        past_clouds.append((nr, nc))
    
    # 4. 비가 내렸던 칸에 대해 비바라기 사용
    for r, c in past_clouds:
        if grid[r][c] == 0:
            continue
        cnt = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < N and 0 <= nc < N):
                continue
            if grid[nr][nc] > 0:
                cnt += 1
        grid[r][c] += cnt
    
    # 5. 구름 생성
    for r in range(N):
        for c in range(N):
            if grid[r][c] >= 2 and (r, c) not in past_clouds:
                grid[r][c] -= 2
                clouds.append([r, c])

ans = 0
for r in range(N):
    ans += sum(grid[r])
print(ans)