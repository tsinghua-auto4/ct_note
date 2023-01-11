"""
Detected time complexity:
O(N * log(N))
"""


def solution(arr):
    n = len(arr)
    if n == 3:
        return arr[0]*arr[1]*arr[2]

    arr_max = max(arr)
    if arr_max == 0:
        return 0

    arr.sort()
    return max(arr[0]*arr[1]*arr[-1],
               arr[-1]*arr[-2]*arr[-3])

