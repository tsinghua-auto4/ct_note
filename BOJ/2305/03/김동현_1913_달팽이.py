
N      = int(input())
target = int(input())

graph = [[0]*N for _ in range(N)]
graph[N//2][N//2] = 1 # 중앙 위치에서 초기화

ans = [-1, -1]

history = 1 # 달팽이가 지나온 길의 숫자를 기억할 메모리
cur = [N//2, N//2] # 달팽이가 전 단계에서 마지막으로 갔던 위치
if history == target:
        ans = cur.copy()

for size in range(3, N+1, 2):
    # 먼저 위로 1 칸
    cur[0] -= 1
    # 우로 끝까지
    for dc in range(size-1):
        history += 1
        if dc != 0:
            cur[1] += 1
        graph[cur[0]][cur[1]] = history

        if history == target:
            ans = cur.copy()
        
    # 하로 끝까지
    for dr in range(1, size):
        history += 1
        cur[0] += 1
        graph[cur[0]][cur[1]] = history

        if history == target:
            ans = cur.copy()
        
    # 좌로 끝까지
    for dc in range(1, size):
        history += 1
        cur[1] -= 1
        graph[cur[0]][cur[1]] = history

        if history == target:
            ans = cur.copy()
        
    # 위로 끝까지
    for dr in range(1, size):
        history += 1
        cur[0] -= 1
        graph[cur[0]][cur[1]] = history

        if history == target:
            ans = cur.copy()
        


for row in graph:
    print(*row)
print(ans[0]+1, ans[1]+1)