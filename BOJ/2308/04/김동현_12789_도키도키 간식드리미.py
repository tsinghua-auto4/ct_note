from collections import deque


N      = int(input())
target = deque(list(map(int, input().split())))

stack  = deque([])
iter   = 1
while target:
    if target and target[0] == iter:
        target.popleft()
        iter += 1
    else:
        stack.append(target.popleft())
    while stack and stack[-1] == iter:
        stack.pop()
        iter += 1

print("Sad" if stack else "Nice")