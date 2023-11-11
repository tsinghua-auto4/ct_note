from collections import deque

def rotate_cw(idx):
    global gears
    
    gear = gears[idx]
    tmp = gear.pop()
    gear.appendleft(tmp)

    gears[idx] = gear

def rotate_ccw(idx):
    global gears
    
    gear = gears[idx]
    tmp = gear.popleft()
    gear.append(tmp)

    gears[idx] = gear


gears = [deque(list(map(int, input()))) for _ in range(4)]

T = int(input())
for _ in range(T):
    idx, dir = map(int, input().split())
    idx -= 1

    list_cw  = [] # 시계방향으로 돌아갈 기어 idx
    list_ccw = [] # 반시계방향으로 돌아갈 기어 idx

    if dir == 1:
        list_cw.append(idx)
    else:
        list_ccw.append(idx)

    # 움직이는 기어 왼쪽부터 첫번째 기어까지 확인
    d = -1*dir
    mem = gears[idx][6]
    for iter in range(idx-1, -1, -1):
        if gears[iter][2] != mem:
            if d == 1:
                list_cw.append(iter)
            else:
                list_ccw.append(iter)
            d  *= -1
            mem = gears[iter][6]
        else:
            break

    # 움직이는 기어 오른쪽부터 마지막 기어까지 확인
    d = -1*dir
    mem = gears[idx][2]
    for iter in range(idx+1, 4):
        if gears[iter][6] != mem:
            if d == 1:
                list_cw.append(iter)
            else:
                list_ccw.append(iter)
            d  *= -1
            mem = gears[iter][2]
        else:
            break

    while list_cw:
        cur = list_cw.pop()
        rotate_cw(cur)
    
    while list_ccw:
        cur = list_ccw.pop()
        rotate_ccw(cur)

ans = 0
score = 1
for idx in range(4):
    if gears[idx][0] == 1:
        ans += score
    score *= 2

print(ans)