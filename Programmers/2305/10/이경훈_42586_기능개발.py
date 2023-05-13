from math import ceil

def solution(ps, ss):
    answer = []
    days_left = []
    cnt = 1
    for p, s in zip(ps, ss):
        days_left.append(ceil((100-p)/s))
    
    for i in range(len(days_left)):
        try:
            if days_left[i] < days_left[i+1]:
                answer.append(cnt)
                cnt = 1
            else:
                days_left[i+1] = days_left[i]
                cnt += 1
        except:
            answer.append(cnt)
            
    return answer