# 맞왜틀 문제임, 다시 푸는 중...

from collections import deque

n, l, r = map(int, input().split(' '))
graph   = [list(map(int, input().split(' '))) for _ in range(n)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
is_move = False


def bfs(c_x, c_y, visited, grpah):
    global is_move
    people = graph[c_x][c_y]
    count = 1
    queue = deque()
    queue.append((c_x, c_y))
    visited[c_x][c_y] = True
    temp = list()
    temp.append((c_x, c_y))

    while queue:
        pop_x, pop_y = queue.popleft()

        for dx, dy in move:
            n_x = pop_x + dx
            n_y = pop_y + dy

            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
                continue

            if visited[n_x][n_y]:
                continue

            if l <= abs(grpah[pop_x][pop_y] - grpah[n_x][n_y]) <= r:
                visited[n_x][n_y] = True
                queue.append((n_x, n_y))
                people += graph[n_x][n_y]
                count += 1
                temp.append((n_x, n_y))

    move_people = people // count

    if count > 1:
        is_move = True
        for x, y in temp:
            graph[x][y] = move_people

answer = 0

while True:
    is_move = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, graph)

    if is_move:
        answer += 1
    else:
        break

print(answer)