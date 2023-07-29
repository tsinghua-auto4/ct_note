import sys

def jump(horse_num: int):
    global N, K, board, horses, move, graph

    # 지금 뛰려는 말, 가장 아래에 있지 않다면 안뛰고 바로 종료
    cr, cc, cm = horses[horse_num]
    if horse_num != graph[cr][cc][0]:
        return False

    # 이동하려는 방향과 새로운 좌표
    dr, dc = move[cm]
    nr, nc = cr+dr, cc+dc

    # 범위를 벗어 났을 경우 방향을 바꾸고, 새롭게 이동하려는 타일이 파란색일 때는 끝내자
    if not(0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
        # 우선 방향전환을 한다
        if 0 <= cm <= 1:
            nm = (cm+1)%2
        else:
            nm = (cm-1)%2 + 2

        horses[horse_num][2] = nm
        dr, dc = move[nm]
        nr, nc = cr+dr, cc+dc
        if not(0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
            return False
    
    # 이동하려는 말들, 원래 위치엔 말들이 없어짐
    moving_horses = []
    moving_horses.extend(graph[cr][cc])
    graph[cr][cc] = []

    # 이동하려는 타일이 빨간색일 때는 말들의 순서를 반대로 뒤집어주자
    # 흰색일때는 그대로이기 때문에 냅둠
    if board[nr][nc] == 1:
        moving_horses = moving_horses[::-1]
    
    # 말들을 하나씩 새로운 위치에 넣으면서, 말들의 위치를 따로 업데이트 해줌
    for horse in moving_horses:
        graph[nr][nc].append(horse)
        horses[horse][:2] = [nr, nc]
    
    # 새로운 위치에 말이 4마리 이상이라면 끝!
    if len(graph[nr][nc]) >= 4:
        return True
    else:
        return False


N, K   = map(int, input().split())
move   = [(0, 1), (0, -1), (-1, 0), (1, 0)]

board  = [list(map(int, input().split())) for _ in range(N)] # 보드 타일의 색상을 저장
graph  = [[[] for _ in range(N)] for _ in range(N)] # 보드의 말 저장

horses = [] # 담겨있는 정보는 말의 위치, 그리고 방향
for idx in range(K):
    r, c, m = map(int, input().split())
    graph[r-1][c-1].append(idx)
    horses.append([r-1, c-1, m-1])

# 1000번의 시도 안에 끝내면 성공이지만, 아니면 -1을 출력함
time = 1
while time <= 1000:
    # 모든 시도엔 말들이 한번씩 뛸 기회가 주어짐
    for jumping_horse in range(K):
        flag = jump(jumping_horse)
        if flag:
            print(time)
            sys.exit()
    time += 1
print(-1)