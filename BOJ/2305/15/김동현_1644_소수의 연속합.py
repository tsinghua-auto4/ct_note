

N = int(input())

# 1. 에라토스테네스의 체로 소수를 제일 빨리 구해보고
a = [False,False] + [True]*(N-1)
primes = []

for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

# 2. 좌/우 포인터로 옮겨다니면서 가능성을 구해보자
lft, rgt = 0, 0
tmp_sum  = 0
ans = 0
while rgt <= len(primes):
    tmp_sum = sum(primes[lft:rgt])
    if tmp_sum == N:
        ans += 1
        rgt += 1
    elif tmp_sum < N:
        rgt += 1
    else:
        lft += 1

print(ans)
