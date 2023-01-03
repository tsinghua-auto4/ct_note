"""
1부터 (N+1) 까지의 정수 중 하나가 없다는 것은
이 숫자 범위의 총합과 주어진 배열의 총합의 차가 사라진 수라는 거
"""


def solution(arr):
    ans = 1
    if not arr:     # 빈 배열 => n = 0, 사라진 숫자 1.
        return ans

    n = len(arr)

    # 배열의 총합과 1~(n+1)까지의 총합 차가 없는 정수
    lack = sum(arr)
    total = (1 + (n+1))*(n+1)//2

    ans = total - lack

    return ans
