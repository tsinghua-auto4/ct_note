import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if not scoville:
            answer = -1
            break
            
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1
        
    return answer