
def interaction_GraphDice(nr: int, nc: int):
    global graph, dice
    # 지도, 주사위 상호작용
    if graph[nr][nc] == 0:
        graph[nr][nc] = dice[3][1]
    else:
        dice[3][1] = graph[nr][nc]
        graph[nr][nc] = 0
    # 주사위 윗면 수 출력
    print(dice[1][1])

def move(cr: int, cc: int, oper: int):
    global graph, dice

    # 동
    if oper == 1:
        # 지도의 새로운 위치
        nr, nc = cr, cc+1
        if not ((0 <= nr < N) and (0 <= nc < M)):
            return cr, cc
        # 주사위 재정의
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
        # 지도, 주사위 상호작용 & 주사위 윗면 수 출력
        interaction_GraphDice(nr, nc)
        return nr, nc
    # 서
    elif oper == 2:
        # 지도의 새로운 위치
        nr, nc = cr, cc-1
        if not ((0 <= nr < N) and (0 <= nc < M)):
            return cr, cc
        # 주사위 재정의
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
        # 지도, 주사위 상호작용 & 주사위 윗면 수 출력
        interaction_GraphDice(nr, nc)
        return nr, nc
    # 북
    elif oper == 3:
        # graph의 새로운 위치
        nr, nc = cr-1, cc
        if not ((0 <= nr < N) and (0 <= nc < M)):
            return cr, cc
        # 주사위 재정의
        dice[2][0], dice[2][2] = dice[1][0], dice[1][2]
        dice[1][0], dice[1][2] = -1, -1
        dice = dice[1:4]+[dice[0]]
        # 지도, 주사위 상호작용 & 주사위 윗면 수 출력
        interaction_GraphDice(nr, nc)
        return nr, nc
    # 남
    elif oper == 4:
        # 지도의 새로운 위치
        nr, nc = cr+1, cc
        if not ((0 <= nr < N) and (0 <= nc < M)):
            return cr, cc
        # 주사위 재정의
        dice[0][0], dice[0][2] = dice[1][0], dice[1][2]
        dice[1][0], dice[1][2] = -1, -1
        dice = [dice[3]]+dice[0:3]
        # 지도, 주사위 상호작용 & 주사위 윗면 수 출력
        interaction_GraphDice(nr, nc)
        return nr, nc


N, M, x, y, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
oper  = list(map(int, input().split())) # east 1, west 2, north 3, south 4

# dice init
dice  = [[-1, 0, -1] for _ in range(4)]
dice[1][0], dice[1][2] = 0, 0
if graph[x][y] != 0:
    dice[3][1] = graph[x][y]
    graph[x][y] = 0

for co in oper:
    x, y = move(x, y, co)