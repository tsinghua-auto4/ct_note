"""
개구리 현 위치 X, 가고 싶은 목적지 위치 Y, 개구리 점프 가능 길이 D
1 <= ((X<=Y), D) <= 1,000,000,000
return: 목적지에 도달할 수 있는 최소 점프 횟수


경우1. X == Y, 점프 안 해도 됨      -> jmp = 0
경우2. D >= Y, 점프 한 번이면 충분    -> jmp = 1
경우3. delta = Y - X, delta % D == 0인 경우와 아닌 경우: 아닌 경우 +1

Detected time complexity:
O(1)
"""


def solution(x, y, d):
    jmp = 0
    if x == y:      # 경우1
        jmp = 0
    elif d >= y:    # 경우2
        jmp = 1
    else:           # 경우3
        delta = y - x
        if delta % d != 0:
            jmp += 1
        jmp += (delta // d)
    return jmp
