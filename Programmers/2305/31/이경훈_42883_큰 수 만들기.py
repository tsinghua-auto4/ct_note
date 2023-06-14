def solution(number, k):
    answer = ''
    stk = []
    
    for i in range(len(number)):
        if not stk or stk[-1] >= number[i]:
            stk.append(number[i])
        else:
            while stk and stk[-1] < number[i] and k > 0:
                stk.pop()
                k -= 1
            stk.append(number[i])
            
    return ''.join(stk[:len(stk)-k])