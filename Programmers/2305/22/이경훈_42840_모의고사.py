def solution(answers):
    answer = []    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        if ans == one[idx%len(one)]:
            score[0] += 1        
        if ans == two[idx%len(two)]:
            score[1] += 1        
        if ans == three[idx%len(three)]:
            score[2] += 1
    
    max_val = max(score)
    
    if max_val == score[0]:
        answer.append(1)
    
    if max_val == score[1]:
        answer.append(2)
        
    if max_val == score[2]:
        answer.append(3)
    
    return answer