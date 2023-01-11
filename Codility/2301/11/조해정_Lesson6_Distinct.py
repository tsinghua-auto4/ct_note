"""
n이 최대 10^5이라, set()으로 치환해서 풀음

Detected time complexity:
O(N*log(N)) or O(N)
"""


def solution(arr):
    n = len(arr)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        arr_set = set(arr)
        return len(arr_set)
