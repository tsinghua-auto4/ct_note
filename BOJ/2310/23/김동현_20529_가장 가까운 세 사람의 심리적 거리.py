from itertools import combinations

T = int(input())
for _ in range(T):
    N    = int(input())
    data = list(map(str, input().split()))
    ans  = float('inf')
    if N > 32:
        print(0)
    else:
        for a, b, c in list(combinations(data, 3)):
            d1, d2, d3 = 0, 0, 0
            for iter in range(4):
                if a[iter] != b[iter]:
                    d1 += 1
                if b[iter] != c[iter]:
                    d2 += 1
                if a[iter] != c[iter]:
                    d3 += 1
            ans = min(ans, d1+d2+d3)
        print(ans)