import sys
from collections import deque

def solution(_board, _visit, _from, _to):
    queue = deque([_from])
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) == _to:
            return
        for i in range(6):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not _visit[nx][ny]:
                    _visit[nx][ny] = True
                    _board[nx][ny] = _board[cx][cy] + 1
                    queue.append((nx, ny))


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

    board = [[0]*n for _ in range(n)]
    visit = [[False]*n for _ in range(n)]

    solution(board, visit, (r1, c1), (r2, c2))
    if board[r2][c2] == 0:
        print(-1)
    else:
        print(board[r2][c2])