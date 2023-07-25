import sys
from collections import deque
queue = deque([])

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    cur = list(map(str, sys.stdin.readline().split()))
    if cur[0] == 'push':
        queue.append(int(cur[1]))
    elif cur[0] == 'pop':
        print(queue.popleft() if len(queue)>0 else -1)
    elif cur[0] == 'size':
        print(len(queue))
    elif cur[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif cur[0] == 'front':
        print(queue[0] if len(queue)>0 else -1)
    elif cur[0] == 'back':
        print(queue[-1] if len(queue)>0 else -1)