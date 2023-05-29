from bisect import bisect_left as bl
N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N

for r in range(N):
    upper_A = A[:r]
    lower_A = list(map(lambda x: -x, A[r:]))

    upper_lis = []
    lower_lis = []

    for a in upper_A:
        if not upper_lis or upper_lis[-1] < a:
            upper_lis.append(a)
        else:
            upper_lis[bl(upper_lis, a)] = a

    for a in lower_A:
        if not lower_lis or lower_lis[-1] < a:
            lower_lis.append(a)
        else:
            lower_lis[bl(lower_lis, a)] = a

    if not upper_lis:
        answer[r] = len(lower_lis)
    elif not lower_lis:
        answer[r] = len(upper_lis)
    else:
        if upper_lis[-1] == -lower_lis[0]:
            answer[r] = len(upper_lis) + len(lower_lis) - 1
        else:
            answer[r] = len(upper_lis) + len(lower_lis)

print(max(answer))