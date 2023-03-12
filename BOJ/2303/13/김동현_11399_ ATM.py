import sys

n    = int(sys.stdin.readline().rstrip())
time = list(map(int, sys.stdin.readline().split()))

time.sort()

sum, mem = 0, 0
for cur in time:
    mem += cur
    sum += mem

print(sum)