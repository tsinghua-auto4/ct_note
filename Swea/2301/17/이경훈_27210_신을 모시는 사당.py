import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

prefix_sum_1 = 0
prefix_sum_2 = 0

max_1 = 0
max_2 = 0

for d in data:
    if d == 1:
        prefix_sum_1 += 1
    else:
        if prefix_sum_1 < 1:
            pass
        else:
            prefix_sum_1 -= 1
    if prefix_sum_1 > max_1:
        max_1 = prefix_sum_1

for d in data:
    if d == 2:
        prefix_sum_2 += 1
    else:
        if prefix_sum_2 < 1:
            pass
        else:
            prefix_sum_2 -= 1
    if prefix_sum_2 > max_2:
        max_2 = prefix_sum_2

print(max_1 if max_1>max_2 else max_2 )