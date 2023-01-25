import sys

input = sys.stdin.readline

def solution():
    target = int(input())
    data   = list(map(int, input().split()))
    ans    = 0

    for cur in data:
        if cur == target:
            ans += 1

    print(ans)


solution()