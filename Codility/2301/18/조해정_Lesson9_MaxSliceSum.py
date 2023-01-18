"""
음수는 더해봤자 더 작아질 뿐이니 0과 더한 맥스값을 비교하기
(하지만 배열이 모두 음수로 이루어져 있다면, 가장 큰 음수 리턴)

Detected time complexity:
O(N)
"""


def solution(arr):
    if len(arr) == 1:
        return arr[0]

    max_ending = 0
    max_slice = 0
    max_elem = -2147483648

    for a in arr:
        max_ending = max(0, max_ending+a)
        max_slice = max(max_slice, max_ending)
        max_elem = max(max_elem, a)

    if max_elem < 0:
        return max_elem
    else:
        return max(max_elem, max_slice)
