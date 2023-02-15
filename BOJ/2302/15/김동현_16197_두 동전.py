import sys
from collections import deque

def InRange(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def solution():
    queue = deque([(coin[0], coin[1], coin[2], coin[3], 0)])
    dr    = [0, 0, 1, -1]
    dc    = [1, -1, 0, 0]

    while queue:
        r1, c1, r2, c2, cnt = queue.popleft()
        if cnt >= 10:
            break

        for i in range(4):
            nr1, nc1 = r1+dr[i], c1+dc[i]
            nr2, nc2 = r2+dr[i], c2+dc[i]
            move     = [1, 1]

            if not InRange(nr1, nc1) and not InRange(nr2, nc2):
                continue
            if not InRange(nr1, nc1) or  not InRange(nr2, nc2):
                return cnt + 1

            if board[nr1][nc1] == '#':
                nr1, nc1 = r1, c1
                move[0]  = 0
            if board[nr2][nc2] == '#':
                nr2, nc2 = r2, c2
                move[1]  = 0
            if move[0] or move[1]:
                queue.append((nr1, nc1, nr2, nc2, cnt+1))

    return -1


if __name__ == "__main__":
    n, m  = map(int, sys.stdin.readline().split())
    board = []
    coin  = []

    for r in range(n):
        board.append(list(sys.stdin.readline().rstrip()))
        for c in range(m):
            if board[r][c] == 'o':
                coin.extend([r, c])

    print(solution())
