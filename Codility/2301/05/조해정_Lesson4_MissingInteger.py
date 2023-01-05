"""
N개의 정수로 구성된 배열 A, A에 없는 가장 작은 자연수를 반환
1 <= N <= 1,000,000
-1,000,000 <= A[i] <= 1,000,000

풀이:
일단 요소 1개이면, 요소 값이 1이면 2 반환, 아니면 1 반환
> 배열 A에서 0과 음수는 고려할 필요가 없으니 가장 작은 자연수가 1인데, 1이 있다면 그 다음인 2
N+1 만큼 False로 구성된 음이 아닌 숫자가 배열에 있는지 판단할 수 있는 배열 생성, False로 초기화, 있다면 True로 갱신
새 배열에서 앞에서부터 순서대로, False이면 기존 배열에 없다는 소리니까 해당 인덱스 반환
다 돌았는데 모두 True이면, 배열 A = [1, 2, ..., N] 라는 소리니까 N+1 반환

Detected time complexity:
O(N) or O(N * log(N))
"""


def solution(arr):
    n = len(arr)

    if n == 1:
        if arr[0] != 1:
            return 1
        else:
            return 2

    not_negative = [False] * (n+1)    # 가능한 음이 아닌 정수가 배열에 있는지 판단 여부, 0은 idx 적기 편하게 추가
    not_negative[0] = True      # 0은 양수가 아니라 반환 못 함

    for i in arr:
        if 0 < i < n+1:     # n 보다 큰 숫자는 고려할 필요 없음, 그럼 무조건 n보다 작은 수가 적어도 하나 이상 없다는 소리
            not_negative[i] = True

    for idx, val in enumerate(not_negative):
        if not val:
            return idx

    return n+1      # 두 번째 for 문이 다 끝나도 반환 못 했다면 1~n까지 다 있다는 소리
