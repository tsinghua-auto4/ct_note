import sys

target = sys.stdin.readline().rstrip()
bomb   = sys.stdin.readline().rstrip()

stack  = []
b_len  = len(bomb)

for idx in range(len(target)):
    stack.append(target[idx])
    if ''.join(stack[-b_len:]) == bomb:
        for _ in range(b_len):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))