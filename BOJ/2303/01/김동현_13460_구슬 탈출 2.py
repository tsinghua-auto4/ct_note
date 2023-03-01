import sys
from collections import deque

def pos_init(_n, _m, _board):# initialize the position of red and blue balls
    global queue, visited
    rx, ry, bx, by = 0, 0 ,0, 0
    flag_r, flag_b = False, False
    for i in range(_n):
        for j in range(_m):
            if _board[i][j] == 'R':
                rx, ry = i, j
            if _board[i][j] == 'B':
                bx, by = i, j
            if flag_r and flag_b:
                break
    queue.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

def move(_x, _y, _dx, _dy, _c, _board):# move untill bump into wall or jump into hole
    while _board[_x + _dx][_y + _dy] != '#' and _board[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1 # moved distance
    return _x, _y, _c

def solution():
    global queue, visited, board

    while queue:
        rx, ry, bx, by, d = queue.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0, board)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0, board)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(d+1)
                return
            # in "# RB" case, as the ball moves to the left, B's delta distance becomes greater than R's.
            # we need to fix B's position, vice-versa
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, d+1))
    print(-1)


if __name__ == "__main__":
    n, m  = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

    # 4th dimension visited, [red_x][red_y][blue_x][blue_x]
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    queue = deque()

    pos_init(n, m, board)
    solution()