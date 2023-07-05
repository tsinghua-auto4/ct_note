

N, M  = map(int, input().split())
board = [list(input()) for _ in range(N)]

ans = 8*8+1
for r_shift in range(N-8+1):
    for c_shift in range(M-8+1):
        tmp1 = 0 # 홀수번 칸이 검은색이 아닌 경우
        tmp2 = 0 # 짝수번 칸이 흰색이 아닌 경우

        for r in range(r_shift, r_shift+8):
            for c in range(c_shift, c_shift+8):
                if (r+c)%2 == 0:
                    if board[r][c] != 'B':
                        tmp1 += 1
                    if board[r][c] != 'W':
                        tmp2 += 1
                else:
                    if board[r][c] != 'B':
                        tmp2 += 1
                    if board[r][c] != 'W':
                        tmp1 += 1
        ans = min(ans, tmp1, tmp2)
print(ans)