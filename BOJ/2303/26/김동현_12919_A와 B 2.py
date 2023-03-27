import sys
import copy

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

#역으로 빼줌, DFS
def check(t):
    if len(t) == len(s):
        return t == s
    
    if t[0] == 'B' and check(t[:0:-1]):
        return True
    if t[-1] == 'A' and check(t[:-1]):
        return True

print(1 if check(t) else 0)