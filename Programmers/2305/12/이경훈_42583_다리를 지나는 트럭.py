from collections import deque

def solution(bridge_length, weight, ts):
    answer = 0
    sum = 0
    time = 0
    
    q = deque([0] * bridge_length)
    
    for i in range(len(ts)):
        while True:
            sum -= q.popleft()
            if sum + ts[i] <= weight:
                sum += ts[i]
                q.append(ts[i])
                time += 1
                break
            else:
                q.append(0)
                time += 1
    return time + bridge_length