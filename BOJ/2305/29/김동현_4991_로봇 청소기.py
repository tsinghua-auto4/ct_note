import sys
from collections import deque

def solution(w: int, h: int, graph: list[list]):
    robot, dusts = (-1,-1), []
    res = sys.maxsize

    for r in range(h):
        for c in range(w):
            if graph[r][c] == 'o':
                robot = (r, c)
            elif graph[r][c] == '*':
                dusts.append((r, c))

    n_dust = len(dusts) # 먼지의 개수
    move   = [(-1, 0), (1, 0), (0, -1), (0, 1)] # bfs 방향
    # 2차원 리스트(r=h, c=w)를 먼지의 2**(n_dust) 만큼 만들자, 치운 먼지의 개수의 최소 step을 구할 수 있다
    visit  = [[[sys.maxsize for _ in range(w)] for _ in range(h)] for _ in range(2**(len(dusts))+1)]

    # queue element 정의, (로봇의 위치 r, 로봇의 위치 c, 치운 먼지의 개수, 이동한 총 길이, 먼지 bitmasking)
    queue = deque([(robot[0], robot[1], 0, 0, 0)])
    while queue :
        cr, cc, cnt, step, dirty_status = queue.popleft()
        
        if cnt == n_dust:
            res = min(step,res)

        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue

            if graph[nr][nc] == '.' or graph[nr][nc] == 'o': # 빈 칸 or 청소기 시작 위치
                    if visit[dirty_status][nr][nc] > step+1: # 지금 masking에서 더 짧은 거리로 올 수 있다면 갱신
                        visit[dirty_status][nr][nc] = step+1
                        queue.append((nr, nc, cnt, step+1, dirty_status))

            elif graph[nr][nc] == '*': # 먼지가 있는 칸일 때
                if dirty_status & (2**dusts.index((nr,nc))) == 0: # 처음 치우는 먼지?
                    next_dirty_status = dirty_status | 2**dusts.index((nr,nc)) # 치운 먼지의 bitmask 갱신
                    visit[next_dirty_status][nr][nc] = step+1 # 이동거리 갱신
                    queue.append((nr, nc, cnt+1 , step+1 , next_dirty_status))

                else: # 치웠던 먼지?
                    if visit[dirty_status][nr][nc] > step+1: # 더 빨리 치울 수 있다면 갱신 
                        visit[dirty_status][nr][nc] = step+1
                        queue.append((nr, nc, cnt, step+1, dirty_status))

    return res if res != sys.maxsize else -1


while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    target = [list(input()) for _ in range(h)]
    print(solution(w, h, target))