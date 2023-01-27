import sys

input = sys.stdin.readline

r1, s = map(int, input().split())
print(s+(s-r1))