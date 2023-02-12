import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
  x, y = input().split()
  data.append((int(x), y))
#print(data)
data.sort(key=lambda x:x[0])
for x, y in data:
  print(x, y)