
def clockwise(target: list):
    return [target[8-1]] + target[:8-1]

def counter_clockwise(target: list):
    return target[1:] + [target[0]]

def turn(target: list, direction: int):
    if direction == 1:
        return clockwise(target)
    else:
        return counter_clockwise(target)

def solution():
    global T, gears, K, turns

    for pos, direction in turns:
        idx = pos - 1 # 인덱싱을 위한 -1
        direction # 1: clockwise, -1: counter-clockwise

        # 맞닿아 있는 극이 다르다면, 반대방향으로 회전
        # 맞닿아 있는 극이 같다면, 회전 X
        
        # 돌린 톱니바퀴의 왼쪽부터 0번째 인덱스의 톱니바퀴를 돌려보자
        cur_direction = direction
        active = gears[idx][6]
        for cur in range(idx-1, -1, -1):
            passive = gears[cur][2]

            # 같은 극이라면 움직이지 않아서 더이상 볼 필요가 없음
            if active == passive:
                break
            
            # 다음 톱니의 액티브를 준비하자
            active = gears[cur][6]
            
            # 톱니를 돌려주자
            cur_direction *= -1
            gears[cur] = turn(gears[cur], cur_direction)


        # 돌린 톱니바퀴 오른쪽부터 마지막 톱니바퀴를 돌려보자
        cur_direction = direction
        active = gears[idx][2]
        for cur in range(idx+1, T):
            passive = gears[cur][6]

            if active == passive:
                break
            
            active = gears[cur][2]

            cur_direction *= -1
            gears[cur] = turn(gears[cur], cur_direction)

        # 이번 for에서 돌릴 톱니바퀴를 돌려주자
        gears[idx] = turn(gears[idx], direction)


    ans = 0
    for gear in gears:
        if gear[0] == 1:
            ans += 1
    
    return ans



T     = int(input())
gears = [list(map(int, input())) for _ in range(T)] # N극은 0, S극은 1
K     = int(input())
turns = [list(map(int, input().split())) for _ in range(K)]

print(solution())