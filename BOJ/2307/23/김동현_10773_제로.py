from collections import deque

K = int(input())
queue = deque()
for _ in range(K):
    cur = int(input())
    if cur == 0:
        queue.pop()
    else:
        queue.append(cur)
print(sum(queue))