"""
비어 있지 않은 배열 A, N개의 홀수인 정수로 구성
1 <= N <= 1,000,000: 최대 백만 길이의 리스트 A
배열 A 내 숫자 K의 범위: 1 <= K <= 1,000,000,000
배열 내 혼자 홀수 번 등장한 숫자를 찾아서 리턴

풀이:
1. 배열 A의 숫자 K에 대응하는 딕셔너리 dic을 만든다.
2. K가 짝수 개이면 1, 홀수 개이면 -1
-> 최대 백만 개, 이백만 번의 연산
3. dic의 item 검사, value=-1인 key(=Answer Number) 찾아서 반환
-> 최대 오십만 개, 백만 번의 연산

Detected time complexity:
O(N) or O(N*log(N))
"""


def solution(A):
    ans = 0

    dic = {}
    for k in A:
        if k not in dic:
            dic[k] = -1
        else:
            dic[k] *= (-1)

    for key, value in dic.items():
        if value != 1:
            ans = key
            break

    return ans
