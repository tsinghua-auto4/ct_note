import sys

input = sys.stdin.readline
N = int(input())
stk = []
fr = []
to = []
nums = []
for i in range(N):
  nums.append(int(input()))

pointer = 0
temp = 0
flag = True
for i in range(len(nums)):
  if nums[i] > temp:
    for p in range(pointer + 1, nums[i] + 1):
      fr.append(p)
      stk.append('+')
    to.append(fr.pop())
    stk.append('-')
    pointer = nums[i]
    temp = nums[i]
  else:
    if fr[-1] == nums[i]:
      to.append(fr.pop())
      stk.append('-')
      temp = nums[i]
    else:
      flag = False
      break

if (flag):
  for buho in stk:
    print(buho)
else:
  print('NO')
