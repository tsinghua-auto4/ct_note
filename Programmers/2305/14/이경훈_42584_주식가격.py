def solution(prices):
    length = len(prices)
    answer = [i for i in reversed(range(length))]
    stack = [0]
    for i in range(1, length):
        while(stack and prices[stack[-1]] > prices[i]):
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    return answer