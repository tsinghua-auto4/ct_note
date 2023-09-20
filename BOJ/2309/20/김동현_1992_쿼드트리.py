def solution(cr, cc, N):
    global grid, ans

    check = grid[cr][cc]
    for i in range(cr, cr + N):
        for j in range(cc, cc + N):
            if check != grid[i][j]:
                check = -1
                break

    if check == -1:
        ans += "("
        solution(cr, cc, N//2)
        solution(cr, cc+N//2, N//2)
        solution(cr+N//2, cc, N//2)
        solution(cr+N//2, cc+N//2, N//2)
        ans += ")"
    elif check == 1:
        ans += '1'
    elif check == 0:
        ans += '0'


N    = int(input())
grid = [list(map(int, input())) for _ in range(N)]

ans = ''
solution(0, 0, N)
print(ans)