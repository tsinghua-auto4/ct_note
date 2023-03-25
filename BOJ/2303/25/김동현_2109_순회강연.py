import sys
import heapq

n       = int(sys.stdin.readline().rstrip())
lecture = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # element form: [pay, date]

lecture.sort(key=lambda x:(x[1])) # sort by date

candidate = []

for cur in lecture:
    heapq.heappush(candidate, cur[0]) # push money in
    if len(candidate) > cur[1]:
        heapq.heappop(candidate) # pop min money

print(sum(candidate))