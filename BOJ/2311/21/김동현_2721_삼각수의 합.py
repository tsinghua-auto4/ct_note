T = int(input())
for _ in range(T):
    cur = int(input())
    res = sum(k*sum(range(k+2)) for k in range(1, cur+1))
    print(res)