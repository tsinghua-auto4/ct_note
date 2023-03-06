import sys
from collections import deque

def solution(walls):
    queue = deque([(7, 0)])
    move  = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    visit = set()

    while queue:
        loop = len(queue)
        for _ in range(loop):
            cx, cy = queue.popleft()
            if cx == 0 and cy == 7:
                print(1)
                exit()
            for dx, dy in move:
                nx, ny = cx+dx, cy+dy
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8 or (nx, ny) in walls or (nx, ny) in visit:
                    continue
                queue.append((nx, ny))
                visit.add((nx, ny))
        loop = len(walls)
        if loop != 0:
            visit = set()
        for _ in range(loop):
            wx, wy = walls.popleft()
            if wx == 7:
                continue
            walls.append((wx+1, wy))
            if (wx+1, wy) in queue:
                queue.remove((wx+1, wy))
    print(0)

graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(8)]

walls = deque()
for i in range(7, -1, -1):
    for j in range(8):
        if graph[i][j] == '#':
            walls.append((i, j))

solution(walls)