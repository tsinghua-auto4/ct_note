import sys
import heapq
input = sys.stdin.readline

mid = []

N = int(input())

left, right = [], []
ans = []

for i in range(N):
    temp = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-temp, temp))
    else:
        heapq.heappush(right, (temp, temp))

    if right and left[0][1] > right[0][1]:
        min = heapq.heappop(right)[1]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))

    ans.append(left[0][1])

for a in ans:
    print(a)