"""
N counter, 0으로 초기화
두 개의 연산:
- increase(X): X번째 값 + 1
- max counter: 리스트 내 모든 값이 최댓값으로 설정

비어 있지 않은 배열 A, 길이는 M
만약에,
    A[K] == X, 1 <= X <= N      -> K = increase(X)
    A[K] == N + 1,              -> K = max counter

배열 A 요소 값 범위: 1 ~ N+1
1 <= N, M <= 1,000,000

풀이:
K = N+1 일때, 매번 모든 배열 요소를 max 값으로 바꾸면 시간 복잡도가 크게 증가한다.
따라서 max counter를 적용할 조건마다 배열을 바꾸는 것이 아닌 마지막 max 값을 따로 저장하고 갱신한다.
increase 연산을 할 때 해당 요소가 max값보다 작으면 max setting이 안 된 것이니 일단 max로 바꿔주고 increase 연산을 한다.
모든 연산이 끝나고, 따로 기억해둔 마지막 max_counter의 max값보다 작은 모든 배열의 요소를 max값으로 바꿔준다.

Detected time complexity:
O(N + M)
"""


def solution(n, arr):
    new_arr = [0] * n
    max_arr = 0     # 배열의 max 값, 상시 갱신
    last_max = 0    # max counter 연산 시만 갱신 되는 그 때의 max 값

    for idx in arr:     # arr 의 각 요소 값이자, 새로운 배열의 인덱스+1 값
        if idx == n+1:
            last_max = max_arr
        else:
            if last_max > new_arr[idx-1]:
                new_arr[idx-1] = last_max   # max counter 연산 직후, 모든 배열 요소는 같은 값이기 때문에 increase 하기 전에 같은 값으로 맞춰야 한다
            new_arr[idx-1] += 1
            max_arr = max(max_arr, new_arr[idx-1])

    for idx, val in enumerate(new_arr):     # 배열의 모든 요소는 최소 max counter 연산 시의 max 값이다
        if val < last_max:
            new_arr[idx] = last_max

    return new_arr
