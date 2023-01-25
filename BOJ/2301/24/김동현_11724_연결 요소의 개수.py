import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution(cur):
    if mark[cur]:
        return

    mark[cur] = True
    for i in link[cur]:
        solution(i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    link = [[] for _ in range(n+1)]
    mark = [False] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)

    ans = 0

    for i in range(1, n+1):
        if not mark[i]:
            ans += 1
            solution(i)

    print(ans)