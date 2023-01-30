import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global n, graph
    queue   = deque([1])
    mark    = [False] * (n+1)
    mark[1] = True

    idx = 1
    while queue:
        cur = queue.popleft()
        sub = []
        for child in graph[cur]:
            if not mark[child]:
                mark[child] = True
                sub.append(child)
        if sorted(seq[idx:idx+len(sub)]) == sorted(sub):
            for child in seq[idx:idx+len(sub)]:
                queue.append(child)
            idx += len(sub)
        else:
            return 0
    return 1


if __name__ == "__main__":
    n     = int(input())
    graph = [[]*(n+1) for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    seq = list(map(int, input().split()))

    if seq[0] == 1:
        print(bfs())
    else:
        print(0)