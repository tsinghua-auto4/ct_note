import sys
import math
input = sys.stdin.readline
m, n = list(map(int, input().split()))
minors = []
for i in range(1, n + 1):
    if i == 2 or i == 3:
        minors.append(i)
        if i >= m:
            print(i)
        continue
    elif i % 2 == 0 or i == 1:
        continue
    is_minor = True
    for minor in minors:
        if i % minor == 0:
            is_minor = False
            break
        if minor > int(math.sqrt(minors[-1])) + 1:
            break
    if is_minor:
        minors.append(i)
        if i >= m:
            print(i)
