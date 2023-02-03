import sys
from collections import deque

def bfs(n, k, mark):
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k:
            return mark[cur]
        
        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < 100001 and not mark[nxt]:
                mark[nxt] = mark[cur] + 1
                queue.append(nxt)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    mark = [0] * 100001
    
    print(bfs(n, k, mark))