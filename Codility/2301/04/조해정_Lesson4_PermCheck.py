"""
비어있지 않은 배열 A, N개의 정수로 구성.
각 요소가 한 번씩만 있는, 연속된 수로 구성된 배열이 순열.
A가 순열인지 아닌지 여부 반환. 맞으면 1, 아니면 0.

1 <= N <= 100,000
1 <= 1,000,000,000 <= 1,000,000,000

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].

풀이 :
최솟값과 배열 개수를 통해 만약 순열일 때의 총합을 구하고, 배열의 총합을 구해서 값 비교.
두 총합이 같다면 순열.
숫자가 중복된 거 걸러내기 위해서 set()
얘는 순열이 1부터 시작해야 한다고 했으니, min이 1이 아니면 순열 X.
"""


def solution(arr):
    min_arr = min(arr)
    if min_arr != 1:
        return 0

    n = len(arr)
    if n == 1:
        return 1
    elif n == 2:
        if abs(arr[0]-arr[1]) == 1:
            return 1
        else:
            return 0

    ans = 0

    if n != len(set(arr)):
        return ans

    sum_arr = sum(arr)
    total = (min_arr + (min_arr + n - 1)) * n // 2

    if total == sum_arr:
        ans = 1

    return ans
