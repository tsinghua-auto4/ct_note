from copy import deepcopy

def rotate(x, d, k):
    for iter in range(x-1, N, x):
        roatated = [0]*M
        if d == 0:
            for ro in range(M):
                roatated[ro] = board[iter][(ro-k+M)%M]
        else:
            for ro in range(M):
                roatated[ro] = board[iter][(ro+k+M)%M]
        board[iter] = roatated

def remove():
    global board
    # data의 조작?은 복사본에서 진행하고 마지막에 복사본을 원본으로 씀
    nboard = deepcopy(board)
    # 원판 내부에서 같은 수 찾기
    for i in range(N): #원판 iterator, i
        for j in range(M): # 원판의 원소 iterrator, j
            if board[i][j] == -1: # 비어있으면 넘어감
                continue
            if board[i][(j - 1 + M) % M] == board[i][j]: # 뒤에 원소와 같다면 같이 지움
                nboard[i][j] = -1
                nboard[i][(j - 1 + M) % M] = -1
            if board[i][(j + 1 + M) % M] == board[i][j]: # 앞에 원소와 같다면 같이 지움
                nboard[i][j] = -1
                nboard[i][(j + 1 + M) % M] = -1
    # 반대로 원판끼리 같은 수 찾기
    for j in range(M):
        for i in range(1, N):
            if board[i][j] == -1: 
                continue
            # 안에서 밖에 있는 원판끼리 비교하는 형식이라서 안쪽은 이미 봤다고 판정
            if board[i-1][j] == board[i][j]:
                nboard[i][j] = -1
                nboard[i-1][j] = -1
    # 고친게 없다면 끝내고
    if board == nboard:
        return False
    # 있다면 원판을 바꿔주고 끝내자
    board = nboard
    return True

def averaging():
    avg = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != -1:
                avg += board[i][j]
                cnt += 1
    if cnt == 0: 
        return
    avg /= cnt
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1: 
                continue
            if board[i][j] > avg:
                board[i][j] -= 1
            elif board[i][j] < avg:
                board[i][j] += 1

# 기본 입력
N, M, T  = map(int, input().split())
board    = [list(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    removable = remove()
    if not removable:
        averaging()

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != -1:
            answer += board[i][j]
print(answer)