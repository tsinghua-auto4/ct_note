import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(cur):
    global ans, n
    mark[cur] = True
    ans.append(cur)

    for i in data[cur]:
        if not mark[i]:
            dfs(i)


def bfs(cur):
    global ans, n
    queue = deque([cur])
    mark[cur] = True

    while queue:
        tmp = queue.popleft()
        ans.append(tmp)
        for i in data[tmp]:
            if not mark[i]:
                mark[i] = True
                queue.append(i)


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    data    = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)
    for i in data:
        i.sort()

    ans = []
    mark = [False] * (n+1)
    dfs(v)
    print(*ans)

    ans = []
    mark = [False] * (n+1)
    bfs(v)
    print(*ans)