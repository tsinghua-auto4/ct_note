import sys

r, c  = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

# r이나 c가 홀수 일때 홀수인 축을 잡고 와리가리로 돌 수 있음, 이해가 안간다면 그림을 그려보자
if r%2 == 1:
    print(('R'*(c-1) + 'D' + 'L'*(c-1) + 'D')*(r//2) + 'R'*(c-1))
elif c%2 == 1:
    print(('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(c//2) + 'D'*(r-1))
# r, c 둘 다 짝수라면 하나의 점을 회피점으로 잡으면 나머지 모든 포인트의 값을 먹을 수 있음, 이것도 그림을 그려보면 이해가 감
# 여기서 주의할 점은, 회피점의 좌표 (x,y)는 "(x+y)%2 == 1" 규칙을 가지고 있음
elif r%2 == 0 and c%2 == 0:
    low = 1000     # 회피점의 값, 제일 작아야함
    pos = [-1, -1] # 회피점의 좌표
    # 회피점을 찾아보자, i가 짝수 홀수인 경우를 나눠볼 때, 회피점은 각각 홀수 짝수여야 규칙에 맞음
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > graph[i][j]:
                    low = graph[i][j]
                    pos = [i, j]
        else: # i % 2 == 1
            for j in range(0, c, 2):
                if low > graph[i][j]:
                    low = graph[i][j]
                    pos = [i, j]
    
    # 회피점 전까지의 열을 잡고 와리가리~
    res = ('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(pos[1]//2)
    x = 2 * (pos[1]//2)
    y = 0
    #회피점 열
    xbound = 2 * (pos[1]//2) + 1
    while x != xbound or y != r - 1:
        # 회피점 열보다 한칸 작으면 우로 이동 후 아래로 이동
        if x < xbound and [y, xbound] != pos:
            x += 1
            res += 'R'
        # 회피점 열이면 좌로 이동 후 아래로 이동
        elif x == xbound and [y, xbound-1] != pos:
            x -= 1
            res += 'L'
        if y != r-1:
            y += 1
            res += 'D'

    res += ('R' + 'U'*(r-1) + 'R' + 'D'*(r-1))*((c-pos[1]-1)//2)

    print(res)