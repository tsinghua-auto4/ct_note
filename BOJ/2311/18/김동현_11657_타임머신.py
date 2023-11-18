
def bellman_ford(start):
    dist[start] = 0

    for i in range(1, N+1):
        for j in range(M):
            cur, des, cost = edges[j]
            if dist[cur] != float('inf') and dist[des] > dist[cur] + cost:
                dist[des] = dist[cur] + cost
                if i == N:
                    return True
    return False


N, M = map(int, input().split())

edges = []
dist  = [float('inf')]*(N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])