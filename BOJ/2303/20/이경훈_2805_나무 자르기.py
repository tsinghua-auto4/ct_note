import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))


def binary_search(start, end):
  if start > end:
    return end
  mid = (start + end) // 2
  sum_val = 0
  for tree in trees:
    if tree > mid:
      sum_val += tree - mid
  if sum_val >= M:
    return binary_search(mid + 1, end)
  elif sum_val < M:
    return binary_search(start, mid - 1)


print(binary_search(0, 1000000001))