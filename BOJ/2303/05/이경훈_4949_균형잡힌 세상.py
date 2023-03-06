import sys

input = sys.stdin.readline

bracket = dict()
bracket['('] = ')'
bracket['['] = ']'

while True:
  stack = []
  breaker = False
  data = input().rstrip()
  if data == '.':
    break
  for i in range(len(data)):
    if data[i] == '[' or data[i] == '(':
      stack.append(data[i])
    elif data[i] == ']' or data[i] == ')':
      if len(stack) == 0 or bracket[stack.pop()] != data[i]:
        breaker = True
        break
  if not breaker and len(stack) == 0:
    print('yes')
  else:
    print('no')
