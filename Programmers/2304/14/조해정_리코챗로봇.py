from collections import deque

answer = 0


def solution(board):
    global answer

    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                queue = [[i, j]]
                visited[i][j] = True
            elif board[i][j] == 'G':
                goal_x, goal_y = i, j

    while queue:
        answer += 1
        queue_temp = deque(queue)
        queue = []

        while queue_temp:
            cur_x, cur_y = queue_temp.popleft()

            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                next_x, next_y = cur_x, cur_y

                while True:
                    stop = [next_x, next_y]
                    next_x += dx
                    next_y += dy

                    # 그 방향으로 계속 진행하면서 장애물을 마주치거나 더 이상 진행할 수 없는 방향인 경우
                    if (next_x < 0 or next_x >= n) or (next_y < 0 or next_y >= m) or board[next_x][next_y] == 'D':
                        if not visited[stop[0]][stop[1]]:
                            visited[stop[0]][stop[1]] = True
                            queue.append(stop)

                        if board[stop[0]][stop[1]] == 'G':
                            return answer

                        break

    return -1
