"""
Detected time complexity:
O(N*log(N))
"""


def solution(arr):
    n = len(arr)
    if n < 3:
        return 0

    ans = 0

    arr.sort()
    for i in range(n-2):
        if arr[i] < 1:
            continue
        if arr[i] + arr[i+1] > arr[i+2]:
            ans = 1
            break

    return ans
