import sys
from collections import deque
from itertools import combinations

def bfs(graph: list[list], positions: list):
    scale = len(graph)
    visit = [[-1]*scale for _ in range(scale)]
    
    ans = 0
    queue = deque()
    for r, c in positions:
        queue.append((r, c, 0))
        visit[r][c] = 1
    while queue:
        cr, cc, step = queue.popleft()
        ans = max(ans, step)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < scale and 0 <= nc < scale):
                continue
            if visit[nr][nc] == -1 and graph[nr][nc] != 1:
                visit[nr][nc] = 1
                queue.append((nr, nc, step+1))
    
    for r in range(scale):
        for c in range(scale):
            if visit[r][c] == -1 and graph[r][c] != 1:
                return sys.maxsize
    
    return ans

def solution(N: int, M: int, graph: list[list]):
    # 0. 바이러스 위치 후보
    virus_candidate = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                virus_candidate.append((r,c))

    # 1. 조합으로 바이러스를 퍼뜨려보자
    ans = sys.maxsize
    for case in combinations(virus_candidate, M):
        case = list(case)
        ans = min(ans, bfs(graph, case))

    return ans if ans != sys.maxsize else -1


N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, labs))