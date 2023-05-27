from collections import deque

def bfs(k: int):
    global graph, W, H
    
    move_horse  = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    move_monkey = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visit = [[[0]*(k+1) for _ in range(W)] for _ in range(H)]

    queue = deque([(0, 0, k)])
    while queue:
        cr, cc, horse_jump = queue.popleft()

        if cr == H-1 and cc == W-1:
            return visit[cr][cc][horse_jump]
        
        if horse_jump > 0:
            for dr, dc in move_horse:
                nr, nc = cr+dr, cc+dc
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if graph[nr][nc] != 1 and visit[nr][nc][horse_jump-1] == 0:
                    visit[nr][nc][horse_jump-1] = visit[cr][cc][horse_jump]+1
                    queue.append((nr, nc, horse_jump-1))

        for dr, dc in move_monkey:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if graph[nr][nc] != 1 and visit[nr][nc][horse_jump] == 0:
                visit[nr][nc][horse_jump] = visit[cr][cc][horse_jump]+1
                queue.append((nr, nc, horse_jump))
    return -1


K     = int(input())
W, H  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

print(bfs(K))