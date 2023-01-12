import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(depth):
    global res

    if depth == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(ans[i] - ans[i+1])
        if tmp > res:
            res = tmp

    for i in range(n):
        if not mark[i]:
            mark[i] = True
            ans.append(data[i])
            dfs(depth+1)
            ans.pop()
            mark[i] = False


if __name__ == "__main__":
    n    = int(input())
    data = list(map(int, input().split()))
    mark = [False] * n

    ans = []
    res = -1

    dfs(0)

    print(res)