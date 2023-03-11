import sys
from collections import deque

def solution(s, t):
    visit = {}
    queue = deque([(s, '')])

    while queue:
        cur, val = queue.popleft()
        if cur == t:
            print(val)
            return
        for nxt in ['*', '+', '-', '/']:
            if nxt == '+' and cur+cur <= t and cur+cur not in visit:
                queue.append((cur+cur, val+nxt))
                visit[cur+cur] = True
            elif nxt == '-' and 0 not in visit:
                queue.append((0, val+nxt))
                visit[0] = True
            elif nxt == '*' and cur*cur <= t and cur*cur not in visit:
                queue.append((cur*cur, val+nxt))
                visit[cur*cur] = True
            elif nxt == '/' and cur != 0 and 1 not in visit:
                queue.append((1, val+nxt))
                visit[1] = True
    print(-1)


s, t = map(int, sys.stdin.readline().split())
if s == t:
    print(0)
    exit(0)

solution(s, t)