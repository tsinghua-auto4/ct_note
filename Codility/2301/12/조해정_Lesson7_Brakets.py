"""
경우1. 비어있는 문자열인 경우, return 1
경우2. 문자열 길이가 홀수이면 완전하지 못하니, return 0
나머지 경우. stack으로 확인
!주의! stack 비었을 때 pop 불가능

Detected time complexity:
O(N)
"""


def solution(string):
    n = len(string)
    if n == 0:
        return 1
    elif n % 2 != 0:
        return 0

    stack = []
    ans = 1
    dic = {"}": "{", "]": "[", ")": "("}

    for i in string:
        stack.append(i)
        if i == "}" or i == "]" or i == ")":
            stack.pop()
            if not stack:
                return 0
            c = stack.pop()
            if dic[i] != c:
                return 0

    if stack:
        ans = 0

    return ans

solution(input())