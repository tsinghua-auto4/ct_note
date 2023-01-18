"""
높이 증가할 때마다 스택에 추가
같은 높이는 패스
높이가 제일 마지막 스택보다 짧으면 새 블럭 있어야 한다는 거니까,
스택에서 해당 블럭 빼고 블럭 개수 추가
스택 안의 블럭 길이가 현재 길이보다 길지 않을 때까지 반복
그러다가 스택이 비게 되거나 새 블럭 길이보다 짧아지면 새 블럭 추가하고 반복 종료
맨 나중에 스택에 쌓여있는 만큼 블럭 개수에 추가

Detected time complexity:
O(N)
"""


def solution(h):
    n = len(h)
    if n == 1:
        return 1

    stack = []
    ans = 0

    for i in h:
        if not stack:
            stack.append(i)
        elif stack[-1] < i:
            stack.append(i)
        elif stack[-1] > i:
            while True:
                ans += 1
                stack.pop()
                if not stack:
                    stack.append(i)
                    break
                elif stack[-1] <= i:
                    if stack[-1] != i:
                        stack.append(i)
                    break
    ans += len(stack)

    return ans
