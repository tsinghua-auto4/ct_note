import sys

def tornado(cx, cy, direction):
    global ans 

    if cy < 0:
        return
    
    total = 0
    for portion, dx, dy in direction:
        nx = cx + dx
        ny = cy + dy
        
        if portion == 0:
            new_sand = grid[cx][cy] - total
        else:
            new_sand = int(grid[cx][cy]*portion)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            grid[nx][ny] += new_sand
        else:
            ans += new_sand


N    = int(sys.stdin.readline().rstrip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 움직이는 방향에 따른 먼지 흝날리는 위치
fly_lft =  [
                                        (0.02, -2,  0),
                        ( 0.1, -1, -1), (0.07, -1,  0), (0.01, -1,  1), 
        (0.05,  0, -2), # alpha          # Y           , X
                        ( 0.1,  1, -1), (0.07,  1,  0), (0.01,  1,  1),
                                        (0.02,  2,  0),
        (0,  0, -1) # 마지막에 알파를 계산하자
        ]
fly_rgt = [(portion,  x, -y) for portion, x, y in fly_lft]
fly_dwn = [(portion, -y,  x) for portion, x, y in fly_lft]
fly_up  = [(portion,  y,  x) for portion, x, y in fly_lft]
fly = {0: fly_lft, 1: fly_dwn, 2: fly_rgt, 3: fly_up}

ans  = 0
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

cx, cy = N//2, N//2

time = 0
for i in range(2*N-1):
    d = i%4
    # 같은 길이 2번을 돌 때 마다 길이가 1 증가
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        dx, dy = move[d]
        nx, ny = cx+dx, cy+dy
        tornado(nx, ny, fly[d])
        cx, cy = nx, ny

print(ans)