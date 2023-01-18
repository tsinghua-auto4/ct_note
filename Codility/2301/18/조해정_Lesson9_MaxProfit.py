"""
순익을 보는 거니까 (뒤-앞)을 우선 계산해주고,
그것의 맥스 슬라이스 값을 보면 된다.

Detected time complexity:
O(N)
"""


def solution(arr):
    if len(arr) <= 1:
        return 0

    ans = 0
    max_profit = 0
    for i in range(1, len(arr)):
        max_profit = max(0, max_profit + arr[i] - arr[i-1])
        ans = max(ans, max_profit)

    return ans
