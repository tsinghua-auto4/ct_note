import heapq

def solution(start):
    dp[start] = 0

    heap  = []
    heapq.heappush(heap, (0, start))

    while heap:
        cw, cn = heapq.heappop(heap)

        if dp[cn] < cw:
            continue

        for nw, nn in graph[cn]:
            new_w = nw+cw

            if new_w < dp[nn]:
                dp[nn] = new_w
                heapq.heappush(heap, (new_w, nn))


INF = float('inf')

V, E = map(int, input().split())
K    = int(input())

dp    = [INF]*(V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

solution(K)
for iter in range(1, V+1):
    print("INF" if dp[iter] == INF else dp[iter])