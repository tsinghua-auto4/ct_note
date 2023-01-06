"""
Detected time complexity:
O(N)
"""

def solution(arr):
    n = len(arr)
    east = []   # 동쪽으로 가는 차량 위치

    for idx, direction in enumerate(arr):
        if direction == 0:  # 서에서 동은 의미가 없으니 패스
            east.append(idx)

    passing = 0     # 지나가는 차
    east_car = 0    # 조회 중인 위치보다 동쪽에 있는 차, 제외하기 위함
    for idx in east[::-1]:
        passing += (((n-1)-idx) - east_car)
        east_car += 1
        if passing > 1000000000:
            passing = -1
            break
    return passing
