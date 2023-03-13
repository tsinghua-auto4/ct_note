import sys

input = sys.stdin.readline

data = []
N = int(input())
for i in range(N):
  temp = int(input().rstrip())
  if temp == 0:
    data.pop()
  else:
    data.append(temp)

sum = 0

for d in data:
  sum += d
print(sum)
