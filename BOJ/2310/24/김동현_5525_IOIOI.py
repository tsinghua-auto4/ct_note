N = int(input()) # N+1 개의 'I', N 개의 'O', 이게 몇 개나 들어있음?
M = int(input()) # S의 길이
S = input()      # target string S

ans, iter, cnt = 0, 0, 0

while iter < (M-1):
    # 훑어 보면서 'IOI' 조각들을 볼 때 마다, cnt+1
    if S[iter: iter+3] == 'IOI':
        iter += 2
        cnt  += 1

        # 그러다 'IOI'의 수가 내가 찾는 것과 같으면, cnt-1하고, ans+1
        if cnt == N:
            ans += 1
            cnt -= 1
    # 없으면 그냥 iter+1, cnt 초기화
    else:
        iter += 1
        cnt   = 0

print(ans)