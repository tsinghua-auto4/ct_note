import sys

input = sys.stdin.readline


def dfs(x, y, step, total):
    global answer

    # 탈출조건1: (나머지 횟수 * 최대 수)가 찾은 answer 보다 작다면 굳이 돌릴 필요가 없음.
    if total + max_val*(4-step) <= answer:
        return

    # 탈출조건2: 4번 다 돌았으면 answer 갱신해주고 끝냄.
    if step == 4:
        answer = max(answer, total)
        return 

    # dfs 시작~
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        # 이동한 새로운 위치가 범위 안에 있어야하고, 아직 안가본 위치여야함
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # I, O, J, S 형 테트로미노와 달리, T형의 경우 ㅏㅓㅗㅜ를 만들 때 새로 찍고 그 전 좌표로 돌아가야함
            if step == 2:
                visited[nx][ny] = True
                dfs(x, y, step+1, total+data[nx][ny])
                visited[nx][ny] = False
            
            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+data[nx][ny])
            visited[nx][ny] = False



if __name__ == "__main__":
    n, m    = map(int, input().split())
    data    = [list(map(int, input().split())) for _ in range(n)]
    max_val = max(map(max, data))
    visited = [[False]*m for _ in range(n)]
    d       = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    answer  = 0

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, data[i][j])
            visited[i][j] = False

    print(answer)