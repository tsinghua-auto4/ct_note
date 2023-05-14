from collections import deque

def solution(ps, l):
    answer = 0
    q = deque()
    
    for idx, p in enumerate(ps):
        q.append((idx, p))
        
    while q:
        max_p = max(sub[1] for sub in q)
        idx, p = q.popleft()
        if max_p == p:
            answer += 1
            if idx == l:
                break
            continue
        q.append((idx, p))
        
    return answer