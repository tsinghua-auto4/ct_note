from collections import deque


def solution(prices):
    len_prices = len(prices)
    answer = [0 for _ in range(len_prices)]

    stack = deque()
    for idx, price in enumerate(prices):
        while stack:
            if price < stack[-1][1]:
                [i, _] = stack.pop()
                answer[i] = idx - i
            else:
                break
        stack.append([idx, price])

    for i, _ in stack:
        answer[i] = (len_prices - 1) - i

    return answer
