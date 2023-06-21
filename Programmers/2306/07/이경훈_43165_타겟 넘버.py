answer = 0

def dfs(cnt, numbers, target, sum_val):
    global answer
    if cnt == len(numbers):
        if sum_val == target:
            answer += 1
        return
    dfs(cnt+1, numbers, target, sum_val + numbers[cnt])
    dfs(cnt+1, numbers, target, sum_val - numbers[cnt])
    
def solution(numbers, target):
    dfs(0, numbers, target, 0)    
    return answer