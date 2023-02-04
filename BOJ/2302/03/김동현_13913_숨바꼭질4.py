import sys
from collections import deque

def path(cur):
    history = []
    tmp = cur

    for _ in range(mark[cur]+1):
        history.append(tmp)
        tmp = move[tmp]
    print(*history[::-1])

def bfs(n, k, mark):
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k:
            print(mark[cur])
            path(cur)
            return
        
        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < 100001 and not mark[nxt]:
                mark[nxt] = mark[cur] + 1
                move[nxt] = cur
                queue.append(nxt)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    mark = [0] * 100001
    move = [0] * 100001
    
    bfs(n, k, mark)