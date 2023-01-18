"""
Detected time complexity:
O(N)
"""


def solution(arr):
    n = len(arr)
    if n == 3:
        return 0

    left = [0] * n
    right = [0] * n

    for i in range(1, n-1): # 맨 처음과 마지막 값은 합계에 절대로 포함되지 않는다
        val_l = arr[i]
        val_r = arr[-i-1]

        # 1번째부터 i번째까지 최대 합, 0보다 작으면 숫자 연속으로 붙여 0으로 초기화
        left[i] = max(0, left[i-1]+val_l)
        # n번째 부터 n-i번째까지 최대 합, 0보자 작으면~
        right[-i-1] = max(0, right[-i]+val_r)

    ans = 0
    # p<q<r, p+1번째부터 q-1번째까지, 그리고 q+1번째부터 r-1번째까지 총합, 그 중에 가장 큰 거
    for i in range(1, n-1):
        ans = max(ans, left[i-1]+right[i+1])
    return ans
