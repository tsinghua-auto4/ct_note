from collections import deque


def dfs(x, y, board, judge, n):
    global lst

    if 0 <= x < n and 0 <= y < n and board[x][y] != judge:
        board[x][y] = judge
        lst.append([x, y])

        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            dfs(x + dx, y + dy, board, judge, n)


def puzzle(board, judge, n):
    global lst
    dic, cnt = {}, 1
    for i in range(n):
        for j in range(n):
            if board[i][j] != judge:
                lst = []
                dfs(i, j, board, judge, n)
                dic[(len(lst), cnt)] = lst[:]
                cnt += 1
    return dic


def rotate90(lst, n):
    return sorted([[y, -1 - x + n] for x, y in lst])


def set_origin(lst, n):
    dx, dy = lst[0]
    return [[x - dx, y - dy] for x, y in lst]


def solution(game_board, table):
    n = len(game_board)

    blank = puzzle(game_board, 1, n)
    for key, value in blank.items():
        temp = [value]
        for i in range(4):
            temp.append(set_origin(rotate90(temp[i], n), n))
        blank[key] = temp[1:]

    tetris = puzzle(table, 0, n)
    for key, value in tetris.items():
        tetris[key] = set_origin(sorted(value), n)

    answer = 0
    for kt, vt in tetris.items():
        for kb, vb in blank.items():
            if kt[0] == kb[0] and vt in vb:
                answer += kt[0]
                del blank[kb]
                break

    return answer
