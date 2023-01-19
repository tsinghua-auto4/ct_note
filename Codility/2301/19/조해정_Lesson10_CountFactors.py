"""
root(n)까지 계산하면 더 이상 인수가 있는지 계산할 필요가 없다.

Detected time complexity:
O(sqrt(N))
"""


def solution(n):
    cnt = 0
    if n == 1:
        return 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if i == j:
                cnt += 1
                break
            cnt += 2
    return cnt
