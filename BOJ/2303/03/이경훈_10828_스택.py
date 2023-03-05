import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
  oper = input().rstrip()
  if 'push' in oper:
    stack.append(oper.split()[1])
  elif 'pop' in oper:
    if(stack):
      print(stack.pop())
    else:
      print(-1)
  elif 'size' in oper:
    print(len(stack))
  elif 'empty' in oper:
    if (stack):
      print(0)
    else:
      print(1)
  elif 'top' in oper:
    if(stack):
      print(stack[-1])
    else:
      print(-1)
