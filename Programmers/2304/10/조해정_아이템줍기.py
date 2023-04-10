def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[0 for _ in range(102)] for __ in range(102)]
    for a, b, c, d in rectangle:
        for i in range(2 * a, 2 * c + 1):
            for j in range(2 * b, 2 * d + 1):
                graph[i][j] = 1

    line_graph = [[False for _ in range(102)] for __ in range(102)]
    for i in range(2, 101):
        for j in range(2, 101):
            if graph[i][j] == 1:
                sum_blocks = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        sum_blocks += graph[ii][jj]
                if sum_blocks != 9:
                    line_graph[i][j] = True

    # 좌표의 단위가 0.5가 되었기 때문에
    x, y = characterX * 2, characterY * 2
    cur = [[x, y]]
    line_graph[x][y] = False

    while [itemX * 2, itemY * 2] not in cur:
        x, y = cur.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if line_graph[x + dx][y + dy]:
                line_graph[x + dx][y + dy] = False
                cur.append([x + dx, y + dy])
                answer += 1

    return (answer // 2 + 1) // 2