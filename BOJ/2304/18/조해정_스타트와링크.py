import sys
input = sys.stdin.readline

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
diff = 1e9


def dfs(idx, depth):
    global diff

    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (power[i][j] + power[j][i])
                elif not visited[i] and not visited[j]:
                    link += (power[i][j] + power[j][i])
        diff = min(diff, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(idx+1, depth+1)
            visited[i] = False
            if diff == 0:
                return


dfs(0, 0)
print(diff)
