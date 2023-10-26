N = int(input())
B = list(map(int, input().split()))

A = []

fv    = B[0]
max_p = 0

for iter in range(N):
    tmp = B[iter]
    p   = 0

    while tmp%3 == 0:
        tmp //= 3
        p += 1
    if (p > max_p) or (p == max_p and B[iter] < fv):
        max_p = p
        fv    = B[iter]
A.append(fv)

for iter in range(N):
    if A[-1]*2 in B:
        A.append(A[-1]*2)
        continue
    elif A[-1]%3==0 and A[-1]//3 in B:
        A.append(A[-1]//3)
        continue
    break

print(*A)