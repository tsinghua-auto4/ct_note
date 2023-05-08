
# 좌우반전
def mirror(cube):
    row = len(cube)
    col = len(cube[0])
    ret = ["" for i in range(row)]
    for r in range(row):
        for c in range(col - 1, -1, -1):
            ret[r] += cube[r][c]
    return ret

# 90도 회전
def rotate(cube):
    row = len(cube[0])
    col = len(cube)
    ret = ["" for i in range(row)]
    for r in range(row):
        for c in range(col - 1, -1, -1):
            ret[r] += cube[c][r]
    return ret

def check(cube, r, c):
    global T, N, a
    for i in range(len(cube)):
        for j in range(len(cube[0])):
            nr = r + i
            nc = c + j
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                return False
            if (int(cube[i][j])) != a[nr][nc]:
                return False
    return True

def solution():
    global T, N, cubes, a
    # 각 경우의 수 탐색
    for cube in cubes:
        # 좌우 반전은 2번
        for mir in range(2):
            # 90도 회전은 4번, 90*4 = 360
            for rot in range(4):
                # graph확인
                for r in range(N):
                    for c in range(N):
                        if check(cube, r, c):
                            print("yes")
                            return
                cube = rotate(cube)
            cube = mirror(cube)
    print("no")
    return


# 11개의 전개 경우의 수
cubes = [
    ["0010", "1111", "0010"],
    ["0100", "1111", "1000"],
    ["0010", "1111", "0100"],
    ["0001", "1111", "1000"],
    ["0001", "1111", "0100"],
    ["11100", "00111"],
    ["1100", "0111", "0010"],
    ["1100", "0111", "0001"],
    ["0010", "1110", "0011"],
    ["0001", "1111", "0001"],
    ["1100", "0110", "0011"]
]
T = 3
N = 6

for _ in range(T):
    a = [list(map(int, input().split())) for _ in range(N)]
    solution()