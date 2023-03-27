import sys

input = sys.stdin.readline

N = int(input())
S = set()
for i in range(N):
  temp = input().split()
  if len(temp) == 2:
    oper, num = temp
    num = int(num)
  else:
    oper = temp[0]

  if oper == 'add':
    S.add(num)
  elif oper == 'check':
    if num in S:
      print(1)
    else:
      print(0)
  elif oper == 'remove':
    S.discard(num)
  elif oper == 'toggle':
    if num in S:
      S.remove(num)
    else:
      S.add(num)
  elif oper == 'all':
    S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
  elif oper == 'empty':
    S.clear()
