def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    new_board = [[0 for _ in range(M+1)] for _ in range(N+1)]
        
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            new_board[r1][c1] -= degree
            new_board[r1][c2+1] += degree
            new_board[r2+1][c1] += degree
            new_board[r2+1][c2+1] -= degree
        else:
            new_board[r1][c1] += degree
            new_board[r1][c2+1] -= degree
            new_board[r2+1][c1] -= degree
            new_board[r2+1][c2+1] += degree
    
    for i in range(N):
        for j in range(1, M):
            new_board[i][j] += new_board[i][j-1]
    
    for i in range(M):
        for j in range(1, N):
            new_board[j][i] += new_board[j-1][i]
            
    for i in range(N):
        for j in range(M):
            board[i][j] += new_board[i][j]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1
    
    return answer