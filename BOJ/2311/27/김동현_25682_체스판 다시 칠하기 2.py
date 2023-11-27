# 블로그 참조함, 혼자 못 풀겠음
def minimal_board(color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    # PTN에 따른 현 위치 타일이 누적 합에 의한 수정 개수를 갱신함
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0: 
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value
    
    # K*K의 크기의 판의 크기를 유지하면서, 누적 합에 의한 최소 수정 개수를 찾음
    count = float('inf')
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            count = min(count, prefix_sum[i + K - 1][j + K - 1] - prefix_sum[i + K - 1][j - 1] - prefix_sum[i - 1][j + K - 1] + prefix_sum[i - 1][j - 1])
    return count


N, M, K = map(int, input().split())
board    = [list(map(str, input())) for _ in range(N)]
print(min(minimal_board('B'), minimal_board('W')))