import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(idx):
    global sign

    cur = 0
    for i in range(idx, -1, -1):
        cur += ans[i]
        if sign[i][idx] == '+' and cur <= 0:
            return
        elif sign[i][idx] == '-' and cur >= 0:
            return
        elif sign[i][idx] == '0' and cur != 0:
            return
    return True

def solution(idx):
    if idx == n:
        print(' '.join(map(str, ans)))
        exit(0)
    for i in range(-10, 11):
        ans.append(i)
        if check(idx):
            solution(idx+1)
        ans.pop()


if __name__ == "__main__":
    n      = int(input())
    target = list(input())

    sign   = [[0] * n for _ in range(n)]
    ans, k = [], 0

    for i in range(n):
        for j in range(i, n):
            sign[i][j] = target[k]
            k += 1

    solution(0)

