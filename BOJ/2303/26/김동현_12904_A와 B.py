import sys
import copy

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

#역으로 빼줌
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        print(1)
        exit(0)

print(0)