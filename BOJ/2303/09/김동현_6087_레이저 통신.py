# 못풀어서 코드 따옴
# 출처는 https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-6087%EB%B2%88-%EB%A0%88%EC%9D%B4%EC%A0%80-%ED%86%B5%EC%8B%A0-1-Python

from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(sx, sy, ex, ey):
    q = deque()
    visited = [[[INF] * 4 for _ in range(w)] for _ in range(h)]

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
            q.append((nx, ny, i))
            visited[nx][ny][i] = 0

    while q:
        x, y, direct = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
                cnt = visited[x][y][direct]
                if direct == 0 or direct == 2:
                    if i == 1 or i == 3:
                        cnt += 1
                else:
                    if i == 0 or i == 2:
                        cnt += 1

                if visited[nx][ny][i] == -1:  # 방문한 적이 없음
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, i))
                else:  # 방문을 했는데 이전 거울개수보다 최솟값이라면
                    if visited[nx][ny][i] > cnt:
                        visited[nx][ny][i] = cnt
                        q.append((nx, ny, i))

    return min(visited[ex][ey])


if __name__ == "__main__":
    w, h = map(int, input().split())

    pos = []
    board = []
    for i in range(h):
        board.append(list(input().strip()))
        for j in range(w):
            if board[i][j] == "C":
                pos.append((i, j))

    print(bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1]))