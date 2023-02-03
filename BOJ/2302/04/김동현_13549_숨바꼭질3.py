import sys
from collections import deque

def bfs(n, k, dist):
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k:
            return dist[cur]

        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < 100001 and dist[nxt] == -1:
                if nxt == cur*2: #순간이동은 0초라서 우선순위가 높음
                    queue.appendleft(nxt)
                    dist[nxt] = dist[cur]
                else:
                    queue.append(nxt)
                    dist[nxt] = dist[cur] + 1


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    dist    = [-1] * 100001
    dist[n] = 0
    
    print(bfs(n, k, dist))