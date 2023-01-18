"""
stack 으로 풀면,
downstream 은 스택에 추가
upstream 일땐 스택이 비어있으면 비교 없이 살아있는 물고기 숫자에 추가
스택이 비어있지 않다면 스택이 비게 되기 전까지 대소 비교
대소 비교해서 크기가 스택 안에 있는 물고기보다 크다면 스택 안 물고기 제거
마지막까지(스택 크기가 0이 될 때까지) 살아남으면 살아있는 물고기 숫자에 추가

Detected time complexity:
O(N)
"""


def solution(a, b):
    if not a:
        return 0

    stack = []
    ans = 0

    for i in range(len(a)):
        if b[i] == 1:
            stack.append(a[i])
        else:
            if not stack:
                ans += 1
                continue
            while stack:
                if a[i] > stack[-1]:
                    stack.pop()
                else:
                    break
            if not stack:
                ans += 1
    ans += len(stack)
    return ans
