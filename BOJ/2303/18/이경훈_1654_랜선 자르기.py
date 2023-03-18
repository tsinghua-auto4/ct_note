import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lan = []
for i in range(K):
  lan.append(int(input()))


def binary_search(start, end):
  if start > end:
    return end

  mid = (start + end) // 2

  lines = 0
  for i in lan:
    lines += i // mid

  if lines >= N:
    return binary_search(mid + 1, end)
  else:
    return binary_search(start, mid - 1)


print(binary_search(1, max(lan)))
