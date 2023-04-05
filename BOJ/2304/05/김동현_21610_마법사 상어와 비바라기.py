import sys
from collections import deque

def solution():
    global ans, cloud

    for moving, time in move:
        # 1. 여기서 움직여서 구름의 위치를 확정
        # 적용해야할 룰은 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다.
        # -> 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.
        cloud_len = len(cloud)
        for _ in range(cloud_len):
            cx, cy = cloud.popleft()
            dx, dy = direction[moving-1]
            nx, ny = cx+dx*time, cy+dy*time
            if not 0 <= nx < n:
                nx %= n
            if not 0 <= ny < n:
                ny %= n
            # 2. 구름의 최종 위치에서 비가 내림, 1증가
            grid[nx][ny] += 1
            cloud.append([nx, ny])

        post_cloud = {}
        # 3. 물이 증가한 칸에 물이 있는 대각선 칸 갯수를 더함
        cloud_len = len(cloud)
        for _ in range(cloud_len):
            cx, cy = cloud.popleft()
            cnt = 0
            for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                nx, ny = cx+dx, cy+dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if grid[nx][ny] > 0:
                    cnt += 1
            grid[cx][cy] += cnt
            post_cloud[(cx, cy)] = 0
        # 4. 구름 clear

        # 5. 물이 2 이상인 바구니 위에서 구름 생성, 물양 2 감소
        for i in range(n):
            for j in range(n):
                if grid[i][j] >= 2 and (i, j) not in post_cloud:
                    grid[i][j] -= 2
                    cloud.append([i ,j])
    
    for cur in grid:
        ans += sum(cur)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #(1, 1)~(N, N)
move = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 비바라기를 하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 구름이 생김, 구름에게 이동을 M번 하라고 함
cloud = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

ans = 0
solution()
print(ans)