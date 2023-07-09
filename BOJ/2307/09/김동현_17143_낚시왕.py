

def solution():
    global R, C, M, grid
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ans = 0  # 낚시한 상어 크기의 합
    pos = -1 # 낚시왕의 현재 열 위치
    for _ in range(C):
        # 1. 낚시왕 오른쪽으로 한칸 이동
        pos += 1

        # 2. 현재 열에서 땅이랑 가장 가까운 상어를 잡자
        for cr in range(R):
            if grid[cr][pos]:
                ans += grid[cr][pos][0][2]
                grid[cr][pos].remove(grid[cr][pos][0])
                break

        # 3. 상어가 이동한다
        # 3-1 상어가 이동함
        new_grid = [[[] for _ in range(C)] for _ in range(R)]
        for cr in range(R):
            for cc in range(C):
                if len(grid[cr][cc]) == 0:
                    continue
                cs, cd, cz = grid[cr][cc][0]

                r, c = cr, cc
                dr, dc = direction[cd]
                for _ in range(cs):
                    nr, nc = r+dr, c+dc
                    if not(0 <= nr < R and 0 <= nc < C):
                        if cd %2 ==0:
                            cd +=1
                        else:
                            cd -= 1
                        dr, dc = direction[cd]
                        nr, nc = r+dr, c+dc
                    r, c = nr, nc
                new_grid[r][c].append([cs, cd, cz])
                
        # 3-2 같은 칸에 상어가 여러마리 있으면 한마리만 남김
        for cr in range(R):
            for cc in range(C):
                if len(new_grid[cr][cc]) > 1:
                    new_grid[cr][cc].sort(key = lambda x: x[2], reverse=True)
                    new_grid[cr][cc] = [new_grid[cr][cc][0]]
        
        for r in range(R):
            for c in range(C):
                grid[r][c] = new_grid[r][c]
    return ans


R, C, M = map(int, input().split())
grid    = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    grid[r-1][c-1].append([s, d-1, z])

print(solution())