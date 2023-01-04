"""
빈 배열이 아닌 배열 A, N개의 정수로 구성
배열 A는 테이프의 숫자를 대표...?

인덱스 위치 P, 0 < P < N, 배열 A를 비어있지 않은 두 배열로 쪼갬: A[:P], A[P:]

P에 따른 두 배열의 합의 차의 절댓값: |sum(A[:P])-sum(A[P:])|, 가장 작은 차이값 반환

2 <= N <= 100,000
A 속 정수 범위 -1,000 ~ 1,000

풀이:
1. 배열의 모든 정수의 합을 구한다 => total
2. P 위치에 따른 차이를 담을 배열을 선언한다. => diffs = [0, diff(1), diff(2), ..., diff(P), ..., diff(N-1), total]
3. diff(1) = total - A[0]*2, diff(2) = total - A[0]*2 - A[1]*2 = diff(1) - A[1]*2, ..., diff(N-1) = diff(N-2) - A[N-2]*2
4. diff를 절댓값 해서 가장 작은 diff 반환. 3과정과 같이 하면 좋음.

Detected time complexity:
O(N)
"""


def solution(arr):
    total = sum(arr)
    n = len(arr)

    diffs = [0] * (n+2)
    diffs[-1] = total
    diffs[1] = total - arr[0]*2

    ans = abs(diffs[1])
    if n == 2:
        return ans
    for i in range(2, n):
        diffs[i] = diffs[i-1] - arr[i-1]*2
        ans = min(abs(diffs[i]), ans)

    return ans
