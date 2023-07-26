from collections import deque

queue = deque()

N = int(input())
for num in range(1, N+1):
    queue.append(num)

for _ in range(N-1):
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[0])