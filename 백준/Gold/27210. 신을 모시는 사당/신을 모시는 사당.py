import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
prefix_sum_1 = [0] * n
prefix_sum_2 = [0] * n

prefix_sum_1[0] = 1 if data[0] == 1 else 0
for i in range(1, n):
    if data[i] == 1: 
        prefix_sum_1[i] = prefix_sum_1[i-1]+1
    else: 
        prefix_sum_1[i] = prefix_sum_1[i-1]-1 if prefix_sum_1[i-1]-1 > 0 else 0

prefix_sum_2[0] = 1 if data[0] == 2 else 0
for i in range(1, n):
    if data[i] == 2: 
        prefix_sum_2[i] = prefix_sum_2[i-1]+1
    else: 
        prefix_sum_2[i] = prefix_sum_2[i-1]-1 if prefix_sum_2[i-1]-1 > 0 else 0

print(max(max(prefix_sum_1), max(prefix_sum_2)))