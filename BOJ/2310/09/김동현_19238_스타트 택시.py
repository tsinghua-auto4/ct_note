from collections import deque


def customer_bfs(tr, tc): # taxi_row, taxi_col
    global N, customers

    q     = deque([(tr, tc)]) # queue의 데이터는 (distance, taxi_row, taxi_col)
    visit = [[0]*N for _ in range(N)]

    cand    = [] # res의 데이터는 (distance, customer_row, custormer_col)
    minDist = float('inf')

    cr, cc = -1, -1
    while q: # 로직 실행, 탐색 중간에 손님이 있다면 res에 넣어주고 계속 진행
        cr, cc = q.popleft()
        if visit[cr][cc] > minDist:
            break
        if (cr, cc) in customers.keys():
            if minDist > visit[cr][cc]:
                minDist = visit[cr][cc]
            cand.append((cr, cc))

        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not(0 <= nr < N and 0 <= nc < N) or visit[nr][nc] != 0 or graph[nr][nc] == 1:
                continue
            
            visit[nr][nc] = visit[cr][cc]+1
            q.append((nr, nc))

    if cand:
        cand.sort()
        s_r, s_c = cand[0]
        return visit[s_r][s_c], s_r, s_c
    else:
        return -1, -1, -1


def destination_bfs(tr, tc): # taxi_row, taxi_col == customer_row, customer_col
    global N, customers

    q     = deque([(tr, tc)]) # queue의 데이터는 (distance, taxi_row, taxi_col)
    visit = [[0]*N for _ in range(N)]

    cr, cc = -1, -1 # 함수 전체의 변수
    while q: # 로직 실행, 탐색 중간에 목적지에 도착할 수 있다면 res 반환
        cr, cc = q.popleft()

        if customers[(tr, tc)] == (cr, cc):
            return visit[cr][cc], cr, cc

        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not(0 <= nr < N and 0 <= nc < N) or visit[nr][nc] != 0 or graph[nr][nc] == 1:
                continue
            
            visit[nr][nc] = visit[cr][cc] + 1
            q.append((nr, nc))

    return visit[cr][cc], cr, cc



move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, F = map(int, input().split())
graph   = [list(map(int, input().split())) for _ in range(N)]

tr, tc   = map(int, input().split())
pos_taxi = (tr-1, tc-1)

customers = {}
for _ in range(M):
    cr, cc, zr, zc = map(int, input().split())
    customers[(cr-1, cc-1)] = (zr-1, zc-1)

ans = F
# 손님들을 모셔보자
for _ in range(M):
    tr, tc = pos_taxi

    dist1, cus_r, cus_c = customer_bfs(tr, tc)
    ans -= dist1
    if dist1 == -1 or ans <= 0:
        ans = -1
        break

    dist2, dest_r, dest_c = destination_bfs(cus_r, cus_c)
    ans -= dist2
    if customers[(cus_r, cus_c)] != (dest_r, dest_c) or ans < 0:
        ans = -1
        break

    ans += dist2*2
    pos_taxi = customers[(cus_r, cus_c)]
    customers.pop((cus_r, cus_c))

print(ans)