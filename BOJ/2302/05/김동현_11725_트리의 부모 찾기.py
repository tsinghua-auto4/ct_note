import sys
sys.setrecursionlimit(10**6)

def dfs(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, tree, parent)


if __name__ == "__main__":
    n      = int(sys.stdin.readline())
    tree   = [[] for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    
    dfs(1, tree, parent)

    for i in range(2, n+1):
        print(parent[i])
