import sys

input = sys.stdin.readline
a, b  = 0, 0

for _ in range(int(input())):
    if int(input()) == 1:
        a += 1
    else:
        b += 1

if a > b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")