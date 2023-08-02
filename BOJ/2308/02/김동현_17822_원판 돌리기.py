import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    cur = list(map(int, sys.stdin.readline().split()))

    if cur[0] == 1:
        stack.append(cur[1])
    elif cur[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif cur[0] == 3:
        print(len(stack))
    elif cur[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)
    elif cur[0] == 5:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)