"""
배열 A, N개의 정수로 구성, 회전 수 K

경우1. 빈 배열 또는 요소가 하나 (N<=1) -> 그대로 반환
경우2. K%N==0 (K가 0이거나 N의 배수) -> 그대로 반환
경우3. K < N -> 오른쪽 K개 + 왼쪽 나머지: A[-K:]+A[:-K]
경우4. K > N -> K %= N, 경우3 동일
경우5. 나눠진 왼쪽 배열 또는 오른쪽 배열의 길이가 1이면?
-> 타입이 int인지 list인지 확인해서 append할지 extend할지 결정

"""

def solution(A, K):
    N = len(A)

    # 빈 배열 또는 요소가 하나
    if N < 2:
        return A
    # K=0 또는 N의 배수라 회전에 의미가 없는 경우
    elif K % N == 0:
        return A
    # K > N인 경우, N의 배수 만큼은 회전에 의미가 없어서 제외
    elif K > N:
        K %= N

    # K에 따라 배열 A를 둘로 쪼갬
    left, right = A[:-K], A[-K:]
    # ans = right arr + left arr, 배열 연결할 때 배열인지 아닌지 확인
    ans = []
    # 오른쪽 배열
    if type(right) == int:
        ans.append(right)
    else:
        ans.extend(right)
    # 그 다음 왼쪽 배열
    if type(left) == int:
        ans.append(left)
    else:
        ans.extend(left)

    return ans

