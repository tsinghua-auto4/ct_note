import sys
from collections import deque

def moving():
    global N, M, K, grid, move

    # 파이어볼 개별로 이동을 관찰해보자
    new_fireball = deque()
    for i in range(N):
        for j in range(N):
            T = len(grid[i][j])
            for _ in range(T):
                m, s, d = grid[i][j].popleft()
                # 이동 방향과 현재위치로 이번 스텝의 마지막 위치를 계산해보자
                dx, dy = move[d]
                nx, ny = i + dx*s, j + dy*s
                # 1번 좌측은 N번, N번 우측은 1번인 규칙을 따르도록하자
                if not (0 <= nx < N):
                    nx %= N
                if not (0 <= ny < N):
                    ny %= N
                # 데이터 잠시 저장
                new_fireball.append((nx, ny, m, s, d))
    
    # 새로운 위치의 파이어볼 저장
    for _ in range(len(new_fireball)):
        nx, ny, m, s, d = new_fireball.popleft()
        grid[nx][ny].append((m, s, d))
    
    # 파이어볼 이동이 완료됐으면, 정산을 시작하자
    for i in range(N):
        for j in range(N):
            # 이 칸에 2개 이상의 파이어볼이 존재할 시, 4개의 파이어볼로 나누어진다.
            volume = len(grid[i][j])
            if volume >= 2:
                direction = []
                m_total = 0
                s_total = 0
                for _ in range(volume):
                    m, s, d = grid[i][j].popleft()
                    m_total += m
                    s_total += s
                    direction.append(d%2)
                # 새로운 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
                m_new = m_total//5
                # -> 질량이 0인 파이어볼은 소멸
                if m_new == 0:
                    continue
                # 새로운 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
                s_new = s_total//volume
                # 합쳐지는 파이어볼의 방향이 모두 홀수/짝수면 방향은 0, 2, 4, 6이 되고, 아니면 1, 3, 5, 7
                d_new = [0, 2, 4, 6]
                for idx in range(volume-1):
                    if direction[idx] != direction[idx+1]:
                        d_new = [1, 3, 5 ,7]
                        break
                for idx in range(4):
                    grid[i][j].append((m_new, s_new, d_new[idx]))


# 입력받은 기본 파라미터들
N, M, K  = map(int, sys.stdin.readline().split())

# 파이어볼 이동을 관찰할 그리드
grid = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    cx, cy, m, s, d = map(int, sys.stdin.readline().split())
    grid[cx-1][cy-1].append((m, s, d)) 

# 파이어볼이 이동할 방향을 미리 저장한 리스트
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 파이어볼 이동
for _ in range(K):
    moving()

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for cur in grid[i][j]:
                ans += cur[0]

print(ans)