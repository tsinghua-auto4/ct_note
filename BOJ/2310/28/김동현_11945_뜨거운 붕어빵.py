N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = input()
    grid.append(row[::-1])

for r in range(N):
    print(grid[r])