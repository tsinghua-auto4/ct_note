# 이건 내가 풀지 못할듯
# 대신 해설을 가져와 봄
# 문제는 빈 그리드에 도미노를 채울 수 있는 방법을 제시하는 것입니다.

# 빈 그리드에 도미노를 채운다는 것을 통해 정리할 수 있는 것은 도미노들이 선택할 수 있는 선택 요소들, 그리드의 빈 칸들이 할당받을 수 있는 요소들이고, 할당 요소들에 대해 선택 요소들을 할당하는 다양한 경우의 수를 살펴봐야 하므로 브루트포스 문제에 해당합니다.

# 선택 요소들인 도미노들을 표현해야 합니다. 선택할 때는 2중 for문으로 선택할 수 있고, 방문 표시는 2차원 행렬에 해줍니다.

# 할당 요소들은 각 빈 칸들이므로 미리 그리드를 순회하면서 리스트화(E) 해줍니다.

# 입력을 받을 땐 스도쿠의 조건들과 도미노 방문 표시를 잘 해줍니다. 이것들은 백트래킹에 사용됩니다. 

# 각 도미노들은 하나씩만 존재하고 중복해서 뽑을 수 없으며 뽑는 순서가 중요하므로 순열 브루트포스에 기반해서 코드를 작성하면 됩니다.

# 각 할당 요소에 대해 2중 for문으로 조건을 만족하는 도미노의 두 수를 뽑은 다음 현재 할당 요소의 우측 or 아래측까지 살펴본 다음 도미노를 할당할 수 있으면 할당하고 다음 할당 요소를 살핍니다. 다음 할당 요소들은 이전 할당 요소들에 의해 할당받기 때문에 이미 채워졌다면 다음 할당 요소로 넘기는 코드가 필요합니다.

def go(cnt, itr):
    find = False
    if cnt == Ecnt:
        print('Puzzle', itr)
        for r in range(9):
            for c in range(9):
                print(A[r][c], end='')
            print()
        return True
    r, c = E[cnt]
    if A[r][c]:
        find = go(cnt + 1, itr)
        return find
    for i in range(9):
        for j in range(9):
            if i == j or Visit[i][j]:
                continue
            for d in dr:
                pair_x, pair_y = r + d[0], c + d[1]
                if 0 <= pair_x < 9 and 0 <= pair_y < 9 and not A[pair_x][pair_y]:
                    if R[r][i] == R[pair_x][j] == C[c][i] == C[pair_y][j] == S[r // 3 * 3 + c // 3][i] == S[pair_x // 3 * 3 + pair_y // 3][j] == 0:
                        A[r][c], A[pair_x][pair_y] = i + 1, j + 1
                        Visit[i][j], Visit[j][i] = 1, 1
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
                            pair_x // 3 * 3 + pair_y // 3][j] = 1, 1, 1, 1, 1, 1
                        find = go(cnt + 1, itr)
                        if find:
                            return find
                        A[r][c], A[pair_x][pair_y] = 0, 0
                        Visit[i][j], Visit[j][i] = 0, 0
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[pair_x // 3 * 3 + pair_y // 3][j] = 0, 0, 0, 0, 0, 0
    return find


itr = 1
while True:
    N = int(input())
    if N == 0:
        break

    dr    = [[0, 1], [1, 0]]
    Visit = [[0] * 9 for _ in range(9)]
    A     = [[0] * 9 for _ in range(9)] # 전체 스도미노쿠
    R     = [[0] * 9 for _ in range(9)] # 행 값 저장
    C     = [[0] * 9 for _ in range(9)] # 열 값 저장
    S     = [[0] * 9 for _ in range(9)] # 구역 값 저장
    E     = [] # 빈 땅 저장
    Ecnt  = 0

    for _ in range(N):
        U, LU, V, LV = input().split()

        U_x, U_y = ord(LU[0]) - ord('A'), int(LU[1]) - 1
        V_x, V_y = ord(LV[0]) - ord('A'), int(LV[1]) - 1

        Visit[int(U) - 1][int(V) - 1], Visit[int(V) - 1][int(U) - 1] = 1, 1 

        A[U_x][U_y], A[V_x][V_y] = int(U), int(V)

        R[U_x][int(U) - 1], R[V_x][int(V) - 1] = 1, 1
        C[U_y][int(U) - 1], C[V_y][int(V) - 1] = 1, 1
        S[U_x // 3 * 3 + U_y // 3][int(U) - 1] = 1
        S[V_x // 3 * 3 + V_y // 3][int(V) - 1] = 1
    
    for i, pos in enumerate(input().split()):
        pos_x, pos_y = ord(pos[0]) - ord('A'), int(pos[1]) - 1
        A[pos_x][pos_y] = i + 1
        R[pos_x][i], C[pos_y][i] = 1, 1
        S[pos_x // 3 * 3 + pos_y // 3][i] = 1
    
    for r in range(9):
        for c in range(9):
            if not A[r][c]:
                E.append([r, c])
                Ecnt += 1
    
    go(0, itr)
    itr += 1