import sys

input = sys.stdin.readline

def solution():
    data = [int(input()) for _ in range(3)]

    target = 1
    for i in data:
        target *= i

    target = str(target)
    ans = [0]*10
    for i in target:
        ans[int(i)] += 1

    for i in ans:
        print(i)

solution()