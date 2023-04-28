
def rotate(target: list):
    global N, M
    
    # 돌릴 바퀴의 길이
    sizes = []
    for cur in range(min(N,M)//2):
        sizes.append(2*((N-2*cur)+(M-2*cur))-4)
    
    # 꼬리잡기
    for cur in range(min(N,M)//2):
        for r in range(R%sizes[cur]):
            tmp = A[cur][cur]

            #상-행
            for i in range(1+cur, M-cur):
                A[cur][i-1] = A[cur][i]
            #우-열
            for i in range(1+cur, N-cur):
                A[i-1][M-1-cur] = A[i][M-1-cur]
            #하-행
            for i in range(1+cur, M-cur):
                A[N-1-cur][M-i] = A[N-1-cur][M-1-i]
            #좌-열
            for i in range(1+cur, N-cur):
                A[N-i][cur] = A[N-1-i][cur]
            
            A[1+cur][cur] = tmp



N, M, R = map(int, input().split())
A       = [list(map(int, input().split())) for _ in range(N)]

rotate(A)
for _ in range(N):
    print(*A[_])