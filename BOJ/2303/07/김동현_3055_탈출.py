import sys
from collections import deque

def solution(r, c, sonic, water, visit):
    move = [(0,-1), (0,1), (-1,0), (1,0)]

    cnt = 0
    while sonic:
        for _ in range(len(water)):
            wx, wy = water.popleft()
            for dx, dy in move:
                nx, ny = wx+dx, wy+dy
                if 0 <= nx < r and 0<= ny < c:
                    if graph[nx][ny] == '.':
                        water.append((nx, ny))
                        graph[nx][ny] = '*'
                        visit[nx][ny] = True
        cnt += 1
        for _ in range(len(sonic)):
            sx, sy = sonic.popleft()
            for dx, dy in move:
                nx, ny = sx+dx, sy+dy
                if 0 <= nx < r and 0 <= ny < c:
                    if not visit[nx][ny] and graph[nx][ny] == '.':
                        sonic.append((nx, ny))
                        visit[nx][ny] = True
                    if graph[nx][ny] == 'D':
                        print(cnt)
                        exit()
    print("KAKTUS")


r, c  = map(int, sys.stdin.readline().split())
graph = []

visit = [[False]*c for _ in range(r)]
sonic, water = deque(), deque()
for i in range(r):
    cur = list(map(str, sys.stdin.readline().rstrip()))
    for j in range(c):
        if cur[j] == 'S':
            sonic.append((i, j))
        if cur[j] == '*':
            water.append((i, j))
        if cur[j] == 'X':
            visit[i][j] = True
    graph.append(cur)

solution(r, c, sonic, water, visit)