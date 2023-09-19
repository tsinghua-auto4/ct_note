def solution(r, c, N):
    color = paper[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if color != paper[i][j]:
                solution(r, c, N//2)
                solution(r, c+N//2, N//2)
                solution(r+N//2, c, N//2)
                solution(r+N//2, c+N//2, N//2)
                return
    if color == 0:
        ans.append(0)
    else:
        ans.append(1)


N     = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

ans = []
solution(0,0,N)
print(ans.count(0))
print(ans.count(1))