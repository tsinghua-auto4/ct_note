def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1
    
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
        
    if left == right:
        answer += 1
    
    return answer