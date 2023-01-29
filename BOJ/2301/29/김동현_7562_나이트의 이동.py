import sys
from collections import deque

input = sys.stdin.readline

def if_inrange(x, y):
    global L
    if 0 <= x < L and 0<= y < L:
        return True
    return False

def solution(cu, ta):
    global graph, ans
    move  = [[-2, -1], [-1, -2], [2, -1], [1, -2], [-2, 1], [-1, 2], [2, 1], [1, 2]]
    queue = deque([cu])

    while queue:
        cx, cy = queue.popleft()
        for nxt in move:
            nx, ny = cx + nxt[0], cy + nxt[1]
            if if_inrange(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[cx][cy] + 1
                if nx == ta[0] and ny == ta[1]:
                    ans = graph[nx][ny]
                    return True
                queue.append([nx, ny])

if __name__ == "__main__":
    L, cur, tar, ans = 0, [], [], 0
    for _ in range(int(input())):
        L   = int(input())
        cur = list(map(int, input().split()))
        tar = list(map(int, input().split()))
        ans = 0

        if cur == tar:
            print(ans)
            continue

        graph = [[0]*L for _ in range(L)]
        graph[cur[0]][cur[1]] = 1

        if solution(cur, tar):
            print(ans-1)
