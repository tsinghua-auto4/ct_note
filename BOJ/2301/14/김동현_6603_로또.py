import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(depth, cur):
    if depth == 6:
        print(*ans)
        return

    for i in range(cur, n):
        ans.append(target[i])
        dfs(depth+1, i+1)
        ans.pop()


if __name__ == "__main__":
    n      = 0
    target = []
    ans    = []

    while True:
        target = list(map(int, input().split()))
        if target[0] == 0:
            break

        n      = target[0]
        target = target[1:]

        dfs(0, 0)
        print()
        ans = []

