from collections import deque

def dec_to_bin(target: int):
    ans = format(target, 'b')
    ans = '0'*(4-len(ans)) + ans
    return ans


def bfs(graph: list[list], visit: list[list], room: int, r: int, c: int):
    # 벽은 남: 2**3, 동: 2**2, 북: 2**1, 서: 2**0 만큼 더함
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visit[r][c] = room
    area = 1
    queue = deque([(r, c)])
    while queue:
        cr, cc = queue.popleft()
        for idx in range(4):
            if graph[cr][cc][idx] == '0': # 벽이 없으면 진행
                dr, dc = move[idx]
                nr, nc = cr+dr, cc+dc # 새로운 좌표
                if not (0 <= nr < M and 0 <= nc < N):
                    continue
                if visit[nr][nc] != -1:
                    continue
                visit[nr][nc] = room
                area += 1
                queue.append((nr, nc))
    
    return area


def solution(N: int, M: int, graph: list[list]):
    # 0. 입력받은 그래프의 모든 그리드를 str(binary) 형식으로 바꿔서 저장한 field로 변환
    field = [['']*N for _ in range(M)]
    for r in range(M):
        for c in range(N):
            field[r][c] = dec_to_bin(graph[r][c])

    # 1. bfs로 방이 몇 개 있고, 각 방의 크기를 구해보자
    room  = 0
    area  = {}
    max_area = -1
    visit = [[-1]*N for _ in range(M)]
    for r in range(M):
        for c in range(N):
            if visit[r][c] != -1:
                continue
            room += 1
            area[room] = bfs(field, visit, room, r, c)
            max_area   = max(max_area, area[room])

    # 2. 하나의 벽을 제거해서 얻을 수 있는 방의 크기는 모든 그리드의 벽을 하나씩 없애보면서 확인한다
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_break_area = -1
    for r in range(M):
        for c in range(N):
            grid = field[r][c]
            for idx in range(4):
                if grid[idx] == '1':
                    dr, dc = move[idx]
                    nr, nc = r+dr, c+dc # 새로운 좌표
                    if not (0 <= nr < M and 0 <= nc < N):
                        continue
                    if visit[nr][nc] == visit[r][c]:
                        continue
                    max_break_area = max(max_break_area, area[visit[nr][nc]]+area[visit[r][c]])
    
    print(room)
    print(max_area)
    print(max_break_area)
    
    return


N, M  = map(int, input().split()) # N: col, M: row
graph = [list(map(int, input().split())) for _ in range(M)]

solution(N, M, graph)