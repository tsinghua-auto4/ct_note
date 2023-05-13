# 문제 설명이 거지 같음, 요구사항 자체는 큰 난이도 X
from collections import deque

def rotate_belt():
    global N, K, belt, dura
    belt.rotate(1)
    dura.rotate(1)

def move_belt():
    global N, K, belt
    duraZeroCNT = 0
    for idx in range(2*N-1, -1, -1):
        if dura[(idx+1)%(2*N)] > 0 and belt[idx] == 1 and belt[(idx+1)%(2*N)] == 0:
            dura[(idx+1)%(2*N)] -= 1
            belt[idx], belt[(idx+1)%(2*N)] = 0, 1
            if dura[(idx+1)%(2*N)] == 0:
                duraZeroCNT += 1
    return duraZeroCNT

def load_belt():
    global N, K, belt
    if dura[0] > 0 and belt[0] == 0:
        belt[0] = 1
        dura[0] -= 1
        if dura[0] == 0:
            return 1
        else:
            return 0
    else:
        return 0

def unload_belt():
    global N, K, belt
    belt[N-1] = 0

def simulation():
    global N, K, belt
    state = 0
    broke = 0
    while True:
        state += 1
        unload_belt()

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다
        rotate_belt()
        unload_belt()

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
        #    ① 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다
        broke += move_belt()
        if broke >= K:
            break
        unload_belt()

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
        broke += load_belt()
        if broke >= K:
            break

    return state


N, K = map(int, input().split())
belt = deque([0]*(2*N))
dura = deque(list(map(int, input().split())))

ans = simulation()
print(ans)