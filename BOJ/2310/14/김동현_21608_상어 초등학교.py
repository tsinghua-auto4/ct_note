import heapq

# 여기서 main logic을 구현해보자
def shark_primary():
    global N, grid, prefer
    
    # 선호도를 입력받은 대로 각 학생의 경우를 계산해보자
    for shark in prefer.keys():
        candidate = [] # 모든 경우를 넣을 list
        for r in range(N):
            for c in range(N):
                if grid[r][c] != 0:
                    continue
                cnt_prefer = 0 # 선호하는 학생이 주변에 얼마나 있는지 확인
                cnt_blank = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if grid[nr][nc] in prefer[shark]:
                        cnt_prefer += 1
                    elif grid[nr][nc] == 0:
                        cnt_blank += 1
                heapq.heappush(candidate, [-cnt_prefer, -cnt_blank, r, c])
        _, _, r, c = candidate[0]
        grid[r][c] = shark


N       = int(input())
satisfy = [0, 1, 10, 100, 1000]
grid    = [[0]*N for _ in range(N)]

prefer = {}
for _ in range(N**2):
    data = list(map(int, input().split()))
    prefer[data[0]] = data[1:]

shark_primary()

ans = 0
for r in range(N):
    for c in range(N):
        shark = grid[r][c]
        if shark not in prefer.keys():
            continue
        cnt   = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if grid[nr][nc] in prefer[shark]:
                cnt += 1

        ans += satisfy[cnt]
print(ans)