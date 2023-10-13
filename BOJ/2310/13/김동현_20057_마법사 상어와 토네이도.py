def tornado(cr, cc, d):
    global ans
    
    if cc < 0:
        return
    
    total = 0
    for a, dr, dc in d:
        nr, nc = cr+dr, cc+dc

        if a == 0:#alpha case
            new_sand = grid[cr][cc] - total
        else:
            new_sand = int(grid[cr][cc]*a)
            total += new_sand

        if 0 <= nr < N and 0 <= nc < N:
            grid[nr][nc] += new_sand
        else:
            ans += new_sand
        # 마지막에 grid[cr][cc] = 0을 안하는 이유는 미래의 값에 영향을 주지 않음으로 굳이 안건듬


N    = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# grid 밖으로 나가는 모래는 ans로 정의
ans = 0
# move를 정의하고 좌/하/우/상 순
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 모래가 흩날리는 비율의 LUT 작성, (흩날리는 방향, 비율)
fly_lft = [ (0.02, -2, 0),
            (0.1, -1, -1), (0.07, -1, 0), (0.01, -1, 1),
            (0.05, 0, -2), # alpha, y
            (0.1, 1, -1), (0.07, 1, 0), (0.01, 1, 1),
            (0.02, 2, 0),
            (0, 0, -1) ]
fly_rgt = [(a, dr, -dc) for a, dr, dc in fly_lft]
fly_up  = [(a, dc, dr) for a, dr, dc in fly_lft]
fly_dwn = [(a, -dc, dr) for a, dr, dc in fly_lft]

fly = {0: fly_lft, 1: fly_dwn, 2: fly_rgt, 3: fly_up}


cr, cc = N//2, N//2 # 최초 위치
tic = 0 #직선방향에서의 길이
# 토네이도의 이동 방향을 구현하는 for문 작성
for i in range(2*N-1):# 변의 길이가 N일 때, 달팽이 경로를 가면 총 (2*N-1)개의 직선이 있음
    # 0. 이동방향 d은 0/1/2/3이 될 수 있게
    d = i%4
    if d == 0 or d == 2:
        tic += 1
    # 1. 이동의 길이만큼 ㄱㄱ
    for _ in range(tic):
        dr, dc = move[d]
        nr, nc = cr+dr, cc+dc
        tornado(nr, nc, fly[d])
        cr, cc = nr, nc

print(ans)