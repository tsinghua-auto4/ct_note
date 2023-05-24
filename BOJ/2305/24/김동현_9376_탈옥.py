import sys
from collections import deque

def bfs(target: list[list], r: int, c: int, h: int, w: int):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visit = [[-1] * (w + 2) for _ in range(h + 2)]
    visit[r][c] = 0

    queue = deque()
    queue.append([r, c])
    
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not(0 <= nr < h+2 and 0 <= nc < w+2):
                continue
            if visit[nr][nc] == -1:
                if target[nr][nc] == '.':
                    visit[nr][nc] = visit[cr][cc]
                    queue.appendleft([nr, nc])
                elif target[nr][nc] == '#':
                    visit[nr][nc] = visit[cr][cc] + 1
                    queue.append([nr, nc])
    return visit


def solution():
    # 입력받자
    h, w  = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    
    # 상근이가 밖에서 문을 열어주는 경우를 고려해서 r, c를 2개씩 늘려줌 -> 밖에서 한바퀴 돌 수 있음
    for r in graph:
        r.insert(0, '.')
        r.append('.')
    graph.insert(0, ['.' for _ in range(w+2)])
    graph.append(['.' for _ in range(w+2)])

    # 죄수들의 위치를 찾아보자
    pos = []
    for r in range(h+2):
        for c in range(w+2):
            if graph[r][c] == '$':
                pos.extend([r, c])
                graph[r][c] = '.'
    r1, c1, r2, c2 = pos

    # 상근이/죄수1/죄수2 별로 한번씩 나가는 시나리오
    visit_1 = bfs(graph, 0,  0,  h, w)
    visit_2 = bfs(graph, r1, c1, h, w)
    visit_3 = bfs(graph, r2, c2, h, w)

    # 각 케이스의 문을 연 횟수를 더하고 최소값을 찾아서 출력
    ans = sys.maxsize
    for r in range(h+2):
        for c in range(w+2):
            if visit_1[r][c] != -1 and visit_2[r][c] != -1 and visit_3[r][c] != -1:
                cnt = visit_1[r][c] + visit_2[r][c] + visit_3[r][c]
                if graph[r][c] == '#': # 만나는 지점이 문이라면, 3명 중 한명만 열어도 되는 상황이니 -2
                    cnt -= 2
                ans = min(ans, cnt)

    return ans


for _ in range(int(input())):
    print(solution())