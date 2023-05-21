import sys
from collections import deque

def bfs(v: int):
    global F, S, G, U, D, visit

    queue = deque([v])
    visit[v] = 1

    while queue:
        cur = queue.popleft()
        if cur == G:
            return visit[G]-1

        up = cur + U
        down = cur - D
        if up <= F and not visit[up]:
            queue.append(up)
            visit[up] = visit[cur] + 1
        if 0 < down and not visit[down]:
            queue.append(down)
            visit[down] = visit[cur] + 1
    
    return "use the stairs"


F, S, G, U, D = map(int, input().split())

visit = [0 for _ in range(F+1)]

print(bfs(S))