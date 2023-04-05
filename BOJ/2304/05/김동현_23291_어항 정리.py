import sys
from collections import deque

# 가장 작은 어항에 물고기 1마리 넣기
def fish_compensation(graph):
    num_min = min(graph[0])
    for i in range(n):
        if graph[0][i] == num_min:
            graph[0][i] += 1

# 가장 왼쪽에 있는 어항 위에 쌓기
def popleft_and_stack(graph):
    pop = graph[0].popleft()
    graph.append(deque([pop]))

# 쌓인 어항들을 시계방향 90도 회전
def rotate_90(bowls):
    new_bowls = [[0]*len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0])-1-i]
    return new_bowls

# 2개 이상 쌓인 어항들을 분리해서 공중부양
def fly_blocks(graph):
    while True:
        # 무슨 의미???
        # -> len(graph) == 날게 될 어항의 행
        # -> len(graph[-1]) == 날게 될 어항의 열
        # 90 도로 꺾었을 때, 
        # 바닥에 남은 어항-쌓인 어항의 너비(돌리면 열) 이 쌓여질 어항 덩어리의 길이보다 길어야함 
        if len(graph) > len(graph[0]) - len(graph[-1]):
            break

        will_fly_blocks = []
        will_fly_blocks_row = len(graph)
        will_fly_blocks_col = len(graph[-1])

        # 쌓인 어항을 좌->우, 아래->위 순으로 층을 구분해서 리스트에 넣어줌
        for i in range(will_fly_blocks_row):
            new_deque = deque()
            for _ in range(will_fly_blocks_col):
                new_deque.append(graph[i].popleft())
            will_fly_blocks.append(new_deque)

        graph = [graph[0]]
        rotated_blocks = rotate_90(will_fly_blocks)
        for row in rotated_blocks:
            graph.append(deque(row))

    return graph

def fix_fish_num(graph):
    dp = [[0] * len(graph[x]) for x in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            for d in move:
                nx = x + d[0]
                ny = y + d[1]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]):
                    # 현재 칸이 인접 칸보다 크다면
                    if graph[x][y] > graph[nx][ny]:
                        d = (graph[x][y] - graph[nx][ny]) // 5
                        if d >= 1:
                            dp[x][y] -= d
                    # 현재 칸이 인접 칸보다 작다면
                    else:
                        d = (graph[nx][ny] - graph[x][y]) // 5
                        if d >= 1:
                            dp[x][y] += d

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] += dp[i][j]

# 다시 어항을 일렬로 놓는다
def put_bowl_in_a_row(graph):
    new_graph = deque()

    # 제일 왼쪽에 있는 열부터 밑에서 부터 위로 하나씩 넣어줌
    for i in range(len(graph[-1])):
        for j in range(len(graph)):
            new_graph.append(graph[j][i])

    # 나머지 바닥에 있는 것도 넣어줌
    for i in range(len(graph[-1]), len(graph[0])):
        new_graph.append(graph[0][i])

    result_list = list()
    result_list.append(new_graph)

    return result_list

# 180 도 회전
def rotate_180_clockwise(graph):
    new_graph = []

    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])

    return new_graph

# 다시 공중부양 작업을 한다. 이번에는 절반을 자르는데 2번 수행한다.
def fly_blocks2(graph):
    left1 = list()
    left2 = list()
    new_deque1 = deque()
    for i in range(n//2):
        new_deque1.append(graph[0].popleft())
    left1.append(new_deque1)
    rotated_left1 = rotate_180_clockwise(left1)
    graph += rotated_left1

    for i in range(2):
        temp_deque = deque()
        for j in range(n//4):
            temp_deque.append(graph[i].popleft())
        left2.append(temp_deque)
    rotated_left2 = rotate_180_clockwise(left2)
    graph += rotated_left2

# 물고기가 가장 많은 어항과 가장 적은 어항의 차이를 구하는 함수
def get_result(graph):
    dq = graph[0]
    result1 = max(dq) - min(dq)
    
    return result1

def solution():
    global board
    fish_compensation(board)         # 제일 작은 어항에 물고기 1마리 추가
    popleft_and_stack(board)         # 먼저 제일 왼쪽 어항을 두번째 어항 위에 쌓음
    board = fly_blocks(board)        # 어항 공중부양, 안에 90도 회전 로직도 포함됨
    fix_fish_num(board)              # 인접한 어항끼리 재분배, (차이//5) > 0 일때 실시
    board = put_bowl_in_a_row(board) # 다시 한 행으로 만들자
    fly_blocks2(board)               # 반에 반 접자
    fix_fish_num(board)              # 인접한 어항끼리 재분배, (차이//5) > 0 일때 실시
    board = put_bowl_in_a_row(board) # 다시 한 행으로 만들자

n, k  = map(int, sys.stdin.readline().split())
board = list()
board.append(deque(list(map(int, sys.stdin.readline().split()))))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans  = 0
while get_result(board) > k:
    ans += 1
    solution()

print(ans)