import sys

input = sys.stdin.readline

N = int(input())
origin = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for t in target:
  if t in origin:
    print(1)
  else:
    print(0)
'''
# 이분탐색으로 구하는 법
origin.sort()
def binary_search(start, end, target):
  while (start <= end):
    mid = (start + end) // 2
    if target == origin[mid]:
      print(1)
      return
    elif target > origin[mid]:
      start = mid + 1
    else:
      end = mid - 1
  print(0)
  return


for t in target:
  binary_search(0, N - 1, t)

'''