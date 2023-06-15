from collections import deque
from itertools import combinations

def bfs(graph: list[list], positions: list, blank: int):
    scale = len(graph)
    visit = [[-1]*scale for _ in range(scale)]
    
    ans = 0
    queue = deque()
    for r, c in positions:
        queue.append((r, c))
        visit[r][c] = 1
    while True:
        length = len(queue)
        if blank == 0 or length == 0:
            if blank == 0:
                return ans
            else:
                return float('inf')
        ans += 1
        for _ in range(length):
            cr, cc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr+dr, cc+dc
            
                if not (0 <= nr < scale and 0 <= nc < scale):
                    continue
                if visit[nr][nc] == -1 and graph[nr][nc] == 0:
                    visit[nr][nc] = 1
                    queue.append((nr, nc))
                    blank -= 1
                elif visit[nr][nc] == -1 and graph[nr][nc] == 2:
                    visit[nr][nc] = 1
                    queue.append((nr, nc))

def solution(N: int, M: int, graph: list[list]):
    # 0. 바이러스 위치 후보
    virus_candidate = []
    blank = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                virus_candidate.append((r,c))
            if graph[r][c] == 0:
                blank += 1

    # 1. 조합으로 바이러스를 퍼뜨려보자
    ans = float('inf')
    for case in combinations(virus_candidate, M):
        case = list(case)
        ans = min(ans, bfs(graph, case, blank))
    return ans if ans != float('inf') else -1


N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, labs))