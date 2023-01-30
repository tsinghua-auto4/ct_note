import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, cnt):
    if mark[x]:
        if cnt - dist[x] >= 3:
            return x
        else:
            return -1
    mark[x] = 1
    dist[x] = cnt
    for y in graph[x]:
        cycle = dfs(y, cnt+1)
        if cycle != -1:
            mark[x] = 2
            if x == cycle:
                return -1
            else:
                return cycle
    return -1

def bfs(n, mark, dist, graph):
    queue = deque()
    for i in range(1, n+1):
        if mark[i] == 2:
            queue.append(i)
            dist[i] = 0
        else:
            dist[i] = -1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if dist[y] == -1:
                queue.append(y)
                dist[y] = dist[x] + 1


if __name__ == "__main__":
    n     = int(input())
    mark  = [0] * (n+1)
    dist  = [0] * (n+1)
    graph = [[] * (n+1) for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    dfs(1, 0) #cycle finder
    bfs(n, mark, dist, graph) #dist calculator
    print(' '.join(map(str, dist[1:])))