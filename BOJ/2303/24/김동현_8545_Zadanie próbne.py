import sys

target = str(sys.stdin.readline().rstrip())
for i in range(len(target)-1, -1, -1):
    print(target[i], end='')