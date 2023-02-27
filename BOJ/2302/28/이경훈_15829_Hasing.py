import sys

input = sys.stdin.readline

L = int(input())
data = list(input().rstrip())
for i in range(len(data)):
  data[i] = ord(data[i]) - ord('a') + 1

sum_val = 0
for i in range(len(data)):
  sum_val += data[i] * (31**i)
print(sum_val%1234567891)