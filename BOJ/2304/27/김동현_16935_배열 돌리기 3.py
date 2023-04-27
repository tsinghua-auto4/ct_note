import copy

def oper_1(target: list):
    return target[::-1]

def oper_2(target: list):
    r   = len(target)
    c   = len(target[0])
    tmp = []
    for _ in range(r):
        tmp.append(target[_][::-1])
    return tmp

def oper_3(target: list):
    r   = len(target)
    c   = len(target[0])
    tmp = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-1-i] = target[i][j]
    return tmp

def oper_4(target: list):
    r   = len(target)
    c   = len(target[0])
    tmp = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[c-j-1][i] = target[i][j]
    return tmp

def oper_5(target: list):
    r   = len(target)
    c   = len(target[0])
    tmp = [[0]*c for _ in range(r)]

    hr, hc = r//2, c//2

    for i in range(0, hr):
        for j in range(0, hc):
            tmp[i][j+hc] = target[i][j]
    for i in range(0, hr):
        for j in range(hc, c):
            tmp[i+hr][j] = target[i][j]
    for i in range(hr, r):
        for j in range(hc, c):
            tmp[i][j-hc] = target[i][j]
    for i in range(hr, r):
        for j in range(0, hc):
            tmp[i-hr][j] = target[i][j]

    return tmp

def oper_6(target: list):
    r   = len(target)
    c   = len(target[0])
    tmp = [[0]*c for _ in range(r)]

    hr, hc = r//2, c//2

    for i in range(0, hr):
        for j in range(0, hc):
            tmp[i+hr][j] = target[i][j]
    for i in range(hr, r):
        for j in range(0, hc):
            tmp[i][j+hc] = target[i][j]
    for i in range(hr, r):
        for j in range(hc, c):
            tmp[i-hr][j] = target[i][j]
    for i in range(0, hr):
        for j in range(hc, c):
            tmp[i][j-hc] = target[i][j]

    return tmp


N, M, R   = map(int, input().split())
A         = [list(map(int, input().split())) for _ in range(N)]
oper_list = list(map(int, input().split()))
oper      = [0, oper_1, oper_2, oper_3, oper_4, oper_5, oper_6]

for cur_oper in oper_list:
    A = oper[cur_oper](A)

for _ in range(len(A)):
    print(*A[_])