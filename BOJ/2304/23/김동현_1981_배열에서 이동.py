# 이해 못했음, 알쏭달쏭
# 풀이코드: https://chldkato.tistory.com/67

from collections import deque

def bfs():
    global N, graph

    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    queue = deque([[0, 0]])

    visit = [[False]*N for _ in range(N)]
    visit[0][0] = True


    while queue:
        c_r, c_c = queue.popleft()

        if c_r == N-1 and c_c == N-1:
            return True

        for d_r, d_c in move:
            n_r, n_c = c_r+d_r, c_c+d_c

            if not(0 <= n_r < N and 0 <= n_c < N):
                continue

            if lft <= graph[n_r][n_c] <= rgt and not visit[n_r][n_c]:
                queue.append([n_r, n_c])
                visit[n_r][n_c] = True

    return False


N     = int(input())

graph = []
l_min, r_max = float('inf'), 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    l_min = min(l_min, min(tmp))
    r_max = max(r_max, max(tmp))
    graph.append(tmp)

l_max = min(graph[0][0], graph[N-1][N-1])
r_min = max(graph[0][0], graph[N-1][N-1])

lft, rgt = l_min, r_min
ans = float('inf')
while l_min <= lft <= l_max and r_min <= rgt <= r_max:
    l_flag, r_flag = False, False
    if bfs():
        ans = min(ans, rgt - lft)
        lft += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            lft += 1
            rgt += 1
        else:
            rgt += 1
            r_flag = 1
print(ans)