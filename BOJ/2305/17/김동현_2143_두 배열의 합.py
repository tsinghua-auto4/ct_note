import sys
from collections import defaultdict

def sum_comb(quant: int, target: list, ans: defaultdict):
    for lft in range(quant):
        for rgt in range(lft+1, quant+1):
            ans[sum(target[lft:rgt])] += 1


T = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)

sum_comb(n, a, a_dict)
sum_comb(m, b, b_dict)

ans = 0
for k in a_dict:
    if (T-k) in b_dict:
        ans += a_dict[k]*b_dict[T-k]

print(ans)