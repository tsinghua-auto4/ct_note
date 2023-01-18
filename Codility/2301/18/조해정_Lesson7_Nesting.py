"""
빈 문자열이면 1 반환
( 이면 스택에 추가, 아니면 빼기
근데 빈 배열이면 더 이상 못 빼고 조건에 부합하지 않으니까 0 반환
문자열 다 돌고 나서도 스택에 남아있는 괄호가 있다면 조건에 부합하지 않으니까 0 반환

Detected time complexity:
O(N)
"""


def solution(s):
    n = len(s)
    if n == 0:
        return 1

    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return 0
            stack.pop()

    if not stack:
        return 1
    else:
        return 0
