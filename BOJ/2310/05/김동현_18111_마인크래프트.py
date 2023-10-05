import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = sys.maxsize
idx = 0

for target in range(257):
    max_target, min_target = 0, 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= target:
                max_target += graph[i][j] - target
            else:
                min_target += target - graph[i][j]
    
    if max_target + b >= min_target:
        if min_target + (max_target * 2) <= ans:
            ans = min_target + (max_target * 2)
            idx = target

print(ans, idx)