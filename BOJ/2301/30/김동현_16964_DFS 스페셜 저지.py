import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(mark, graph, seq, x):
    cur = seq.popleft()
    if not seq:
        print(1)
        exit(0)
    mark[cur] = True
    for _ in range(len(graph[cur])):
        if seq[0] in graph[cur] and not mark[seq[0]]:
            dfs(mark, graph, seq, seq[0])
    return False


n     = int(sys.stdin.readline())
mark  = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

seq = deque(map(int, sys.stdin.readline().split()))

if seq[0] != 1:
    print(0)
    exit(0)
if not dfs(mark, graph, seq, 1):
    print(0)
