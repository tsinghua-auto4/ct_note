import sys
from collections import deque

input = sys.stdin.readline

def if_inrange(x, y):
    if 0 <= x and x < n:
        if 0 <= y and y < m:
            return True
    return False

def solution(x, y):
    global graph, n, m
    move  = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        for nxt in move:
            nx, ny = x + nxt[0], y + nxt[1]
            if not if_inrange(nx, ny) or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


if __name__ == "__main__":
    n, m  = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]

    print(solution(0, 0))