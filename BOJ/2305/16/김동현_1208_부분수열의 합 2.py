from itertools import combinations
from collections import defaultdict # 없는 key의 value는 0

# 부분수열의 합
def sub_sum(target: list, ans: defaultdict):
    for cnt in range(1, len(target)+1):
        for comb in combinations(target, cnt):
            comb_sum = sum(comb)
            ans[comb_sum] += 1
            # if comb_sum in ans:
            #     ans[comb_sum] += 1
            # else:
            #     ans[comb_sum] = 1


N, S = map(int, input().split())
data = list(map(int, input().split()))

sub_sum1 = defaultdict(int)
sub_sum2 = defaultdict(int)
# sub_sum1 = dict()
# sub_sum2 = dict()

sub_sum(data[N//2:], sub_sum1)
sub_sum(data[:N//2], sub_sum2)

# S의 경우를 더하기
ans = sub_sum1[S] + sub_sum2[S]
# ans = 0
# if S in sub_sum1:
#     ans += sub_sum1[S]
# if S in sub_sum2:
#     ans += sub_sum2[S]
# 앞 뒤 조합으로 S의 경우의 수끼리 곱해서 모든 경우의 수를 더하자
for s1 in sub_sum1:
    if S-s1 in sub_sum2:
        ans += sub_sum1[s1]*sub_sum2[S-s1]
print(ans)