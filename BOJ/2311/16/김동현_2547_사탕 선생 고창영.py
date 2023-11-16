T = int(input())
input()
for iter in range(T):
    N = int(input())
    cnt = 0
    for _ in range(N):
        tmp = int(input())
        cnt += tmp%N
    cnt %= N
    if cnt == 0:
        print("YES")
    else:
        print("NO")
    if iter < T-1:
        input()