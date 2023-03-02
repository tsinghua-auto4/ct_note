import sys
from collections import deque

def solution():
    global ladder, snake, board, visit

    queue = deque([1])
    visit[1] = True
    while queue:
        cur = queue.popleft()

        for i in range(1, 7):
            nxt = cur + i
            if 0 < nxt <= 100 and not visit[nxt]:
                if nxt in ladder.keys():
                    nxt = ladder[nxt]
                if nxt in snake.keys():
                    nxt = snake[nxt]
                if not visit[nxt]:
                    visit[nxt] = True
                    board[nxt] = board[cur] + 1
                    queue.append(nxt)


if __name__ == "__main__":
    n ,m  = map(int, sys.stdin.readline().split())
    board = [0]*101
    visit = [False]*101

    ladder = {}
    snake  = {}

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        ladder[a] = b
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        snake[a] = b

    solution()
    print(board[100])