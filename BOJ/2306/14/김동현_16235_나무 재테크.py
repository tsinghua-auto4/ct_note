def first_half(A: list[list], field: list[list], point: list[list]):
    global N, M, K
    for r in range(N):
        for c in range(N):
            if len(field[r][c]) == 0:
                continue
            cur = field[r][c]
            cur.sort()
            length = len(cur)
            new_point = 0
            dead_tree = 0
            for idx in range(length):
                if point[r][c] >= cur[idx]:
                    point[r][c] -= cur[idx]
                    cur[idx] += 1
                else:
                    new_point += cur[idx]//2
                    dead_tree += 1
            point[r][c] += new_point
            for _ in range(dead_tree):
                cur.pop()
            field[r][c] = cur


def second_half(A: list[list], field: list[list], point: list[list]):
    global N, M, K
    for r in range(N):
        for c in range(N):
            for cur in field[r][c]:
                if cur%5 == 0:
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        field[nr][nc].append(1)
            point[r][c] += A[r][c]


def simulator(A: list[list], field: list[list], point: list[list]):
    global N, M, K
    # 전반기 하반기
    for _ in range(K):
        first_half(A, field, point)
        second_half(A, field, point)
    # 총합
    ans = 0
    for r in range(N):
        for c in range(N):
            ans += len(field[r][c])
    return ans


N, M, K = map(int, input().split())
A       = [list(map(int, input().split())) for _ in range(N)]
field   = [[list() for _ in range(N)] for _ in range(N)]
point   = [[5]*N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    field[x-1][y-1].append(z)

print(simulator(A, field, point))