from collections import deque


def solution(maps):
    # 동서남북
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    n = len(maps)
    m = len(maps[0])

    loc = deque([])
    loc.append([0, 0])

    while loc:
        x, y = loc.popleft()
        for dx, dy in move:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1:
                loc.append([xx, yy])
                maps[xx][yy] += maps[x][y]
        if maps[-1][-1] != 1:
            break

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]
