import sys

def solution():
    for _ in range(int(sys.stdin.readline())):
        a, b = map(int, sys.stdin.readline().split(','))
        print(a+b)

solution()