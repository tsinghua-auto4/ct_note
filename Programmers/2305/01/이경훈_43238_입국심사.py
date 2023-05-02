def solution(n, times):
    answer = 0
    
    left, right = min(times), n * min(times)
    
    while left <= right:
        mid = (left + right) // 2
        
        people = 0
        
        for time in times:
            people += mid // time
        
        if people >= n:
            answer = mid
            right = mid - 1            
        else:
            left = mid + 1 
    
    return answer