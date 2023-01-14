import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, profit):
    global res, n

    if cur == n:
        res = max(res, profit)
        return

    dfs(cur+1, profit)
    
    t, p = data[cur]
    if cur + t <= n:
        dfs(cur + t, profit + p)



if __name__ == "__main__":
    n    = int(input())
    data = [list(map(int, input().split())) for _ in range (n)]

    res  = 0
    ans  = []

    dfs(0, 0)
    print(res)