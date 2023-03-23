import sys
import heapq

n      = int(sys.stdin.readline().rstrip())
lesson = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lesson.sort(key=lambda x: (-x[0], x[1])) # pay, day

max_date = 0
for cur in lesson:
    if cur[0] > max_date:
        max_date = cur[0]

cur_date = 0
max_money = 0
greedy = []
while cur_date <= max_date:
    cur_date += 1
    while lesson and lesson[0][1] <= cur_date:
        heapq.heappush(greedy, (-lesson[0][0], lesson[0][1]))
        heapq.heappop(lesson)
    if greedy:
        while greedy:
            cur = heapq.heappop(greedy)
            if cur[1] >= cur_date:
                max_money -= cur[0]
                print(cur)
                break

print(max_money)