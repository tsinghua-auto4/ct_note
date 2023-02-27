import sys

input = sys.stdin.readline

T = int(input())
parent = dict()
parent['('] = 1
parent[')'] = -1


for i in range(T):
  sum = 0
  flag = True
  for j in input().rstrip():
    sum += parent[j]
    if sum <0:
      flag = False

  if sum != 0:
    flag = False
  if(flag):
    print('YES')
  else:
    print('NO')