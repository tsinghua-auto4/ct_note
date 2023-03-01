import sys
from copy import deepcopy

def move(_board, direction):
    if direction == 0: #rgt
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                # 숫자가 있으면, 먼저 복사하고 빼줌
                if _board[i][j]:
                    tmp = _board[i][j]
                    _board[i][j] = 0
                    # 지금 조회하고 있는 top이 비었으면 복사한걸 넣어줌, top에 숫자만 채웠기 때문에 idx는 변화 X
                    if _board[i][top] == 0:
                        _board[i][top] = tmp
                    # 지금 조회하고 있는 top이 복사한 값과 같다면 2배를 넣어줌, top의 숫자가 변했기 때문에 idx 변화
                    elif _board[i][top] == tmp:
                        _board[i][top] = tmp * 2
                        top -= 1
                    # 지금 조회하고 있는 top이 복사한 값과 연산이 불가하다면, top을 바꾸는 목적으로 idx 변화,
                    # tmp가 연산에 참여하지 않았음으로 다시 넣어줌
                    else:
                        top -= 1
                        _board[i][top] = tmp
    elif direction == 1: #lft
        for i in range(n):
            top = 0
            for j in range(1, n):
                if _board[i][j]:
                    tmp = _board[i][j]
                    _board[i][j] = 0
                    if _board[i][top] == 0:
                        _board[i][top] = tmp
                    elif _board[i][top] == tmp:
                        _board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        _board[i][top] = tmp
    elif direction == 2: #down
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if _board[i][j]:
                    tmp = _board[i][j]
                    _board[i][j] = 0
                    if _board[top][j] == 0:
                        _board[top][j] = tmp
                    elif _board[top][j] == tmp:
                        _board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        _board[top][j] = tmp
    else: #up
        for j in range(n):
            top = 0
            for i in range(1, n):
                if _board[i][j]:
                    tmp = _board[i][j]
                    _board[i][j] = 0
                    if _board[top][j] == 0:
                        _board[top][j] = tmp
                    elif _board[top][j] == tmp:
                        _board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        _board[top][j] = tmp
    return _board

def solution(_board, depth):#dfs로 모든 경우의 수를 탐색
    global ans

    if depth == 5:
        for i in range(n):
            for j in range(n):
                ans = max(_board[i][j], ans)
        return

    for i in range(4):
        tmp_board = move(deepcopy(_board), i)
        solution(tmp_board, depth+1)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    ans = 0
    solution(board, 0)
    print(ans)