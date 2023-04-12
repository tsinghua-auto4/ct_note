# N: 지금 넣은 삼각형의 크기, n: 최종 크기, pre: 지금 크게 벌릴 삼각형의 크기
def recursive(N: int, n: int, pre: list):
    post = [[" "]*(2*2*N -1) for _ in range(2*N)] # 변의 길이
    for i in range(N): # 맨 위에 있는 삼각형을 만들어주자
        post[i][N : N + 2*N -1] = pre[i]

    j = 0
    for i in range(N, 2*N): # 밑에 깔려 있는 삼각형 2개를 만들어주자
        post[i][:2*N] = pre[j] # 좌측
        post[i][2*N: 2*N + len(pre[j])] = pre[j] # 우측
        j += 1

    if 2*N == n:
        return post

    return recursive(2*N, n, post)


n     = int(input())
basic = [
            [" ", " ", "*", " ", " "], 
            [" ", "*", " ", "*", " "], 
            ["*", "*", "*", "*", "*"]
        ]

if n == 3:
    result = basic
else:
    result = recursive(3, n, basic)

for i in result:
    print("".join(i))