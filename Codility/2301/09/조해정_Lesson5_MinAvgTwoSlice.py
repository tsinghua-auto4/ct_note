"""
풀이:
(a+b)가 (c+d)보다 크거나 같다고 가정하자.
그럼 (a+b+c+d)는 2(a+b)보다 크거나 같다.
반대여도 4개의 변수의 합은 2개의 변수의 합의 2배보다 크거나 같다.
그러니 평균을 구할 때 두 개 변수의 평균과, 세 개 변수의 평균까지만 구하면 된다는 뜻이다.

Detected time complexity:
O(N)
"""


def solution(arr):
    # 0 <= p < q < n, pq는 arr 인덱스
    n = len(arr)

    ans = 0

    min_avg = (arr[0] + arr[1]) / 2

    for p in range(0, n-1):
        sum2 = arr[p] + arr[p+1]
        mean2 = sum2 / 2
        if min_avg > mean2:
            ans = p
            min_avg = mean2

    for p in range(0, n-2):
        sum3 = arr[p] + arr[p+1] + arr[p+2]
        mean3 = sum3 / 3
        if min_avg > mean3:
            ans = p
            min_avg = mean3

    return ans
