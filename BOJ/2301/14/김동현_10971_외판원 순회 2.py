import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start,cur,cost):
    global  s, mark, res

    if start == cur and mark.count(False) == 0:
        res = min(res,cost)


    for i in range(n):
        if not s[cur][i] == 0 and not mark[i]:
            mark[i] = True
            dfs(start,i,cost+s[cur][i])
            mark[i] = False


if __name__ == "__main__":
    n    = int(input())
    s    = [list(map(int, input().split())) for i in range(n)]

    mark = [False] * n
    ans  = [0]
    res  = sys.maxsize
    tmp  = 0

    dfs(0,0,0)
    print(res)