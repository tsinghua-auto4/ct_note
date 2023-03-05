import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
  oper = input().rstrip()
  if 'push_front' in oper:
    queue.appendleft(oper.split()[1])
  elif 'push_back' in oper:
    queue.append(oper.split()[1])  
  elif 'pop_front' in oper:
    if(queue):
      print(queue.popleft())
    else:
      print(-1)
  elif 'pop_back' in oper:
    if(queue):
      print(queue.pop())
    else:
      print(-1)
  elif 'size' in oper:
    print(len(queue))
  elif 'empty' in oper:
    if (queue):
      print(0)
    else:
      print(1)
  elif 'front' in oper:
    if(queue):
      print(queue[0])
    else:
      print(-1)
  elif 'back' in oper:
    if(queue):
      print(queue[-1])
    else:
      print(-1)
