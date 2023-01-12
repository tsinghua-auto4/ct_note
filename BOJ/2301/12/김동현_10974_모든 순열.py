import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(depth):
    if depth == n:
        print(*ans)
        return
    
    for i in range(n):
        if not mark[i]:
            mark[i] = True
            ans.append(data[i])
            dfs(depth+1)
            ans.pop()
            mark[i] = False


if __name__ == "__main__":
    n = int(input())
    data = [i + 1 for i in range(n)]
    mark = [False] * n

    ans = []
    dfs(0)