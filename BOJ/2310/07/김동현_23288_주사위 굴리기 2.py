from collections import deque

def move_dice(dir):
    global dice

    if dir == RIGHT:
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = tmp
    elif dir == LEFT:
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = tmp
    elif dir == UP:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif dir == DOWN:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp

def get_score(sr, sc, B):
    used = [[False] * M for _ in range(N)]
    cnt = 0
    q = deque()
    q.append((sr, sc))
    used[sr][sc] = True
    while q:
        r, c = q.pop()
        cnt += 1 # count 추가
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nc < 0 or nr >= N or nc >= M or used[nr][nc]:
                continue
            if board[nr][nc] == B:
                used[nr][nc] = True
                q.append((nr, nc))
    return cnt * B

N, M, K = map(int, input().split())
board   = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [ 0,-1, 0, 1]
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3

dir  = RIGHT # 현재 방향, 기본 동쪽
dice = [
    [ -1,  2, -1],
    [  4,  1,  3],
    [ -1,  5, -1],
    [ -1,  6, -1]
]

loc = [0, 0]

# 주사위를 굴린다
score = 0
for _ in range(K):
    True
    # 1. 일단 지금 방향대로 굴린다
    nr = loc[0] + dr[dir]
    nc = loc[1] + dc[dir]
    # 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        dir = (dir + 2) % 4
        nr = loc[0] + dr[dir]
        nc = loc[1] + dc[dir]

    # 2. 새로운 바닥면 숫자로 현재 칸과 비교해서 새로운 이동방향과 다이스 객체를 정의함
    loc = (nr, nc)
    move_dice(dir)
    B = board[nr][nc]

    A = dice[3][1]
    if A > B: 
        dir = (dir - 1) % 4
    elif A < B:
        dir = (dir + 1) % 4

    # 3. dfs로 상하좌우 방향으로 최대 이동가능 칸 세서 score에 더해주자
    cur = get_score(nr, nc, B)
    score += cur

print(score)