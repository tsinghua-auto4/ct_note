import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx, depth):
    global ans
    mark[idx] = True
    if depth == 4:
        ans = True
        return
        
    for i in link[idx]:
        if not mark[i]:
            dfs(i, depth+1)
            mark[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    link = [[] for _ in range(n)]
    mark = [False] * 2001
    ans  = False

    for _ in range(m):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)

    for i in range(n):
        dfs(i, 0)
        mark[i] = False
        if ans:
            break
    
    if ans:
        print(1)
    else:
        print(0)