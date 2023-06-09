from itertools import permutations

def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    for route in permutations(dungeons, length):
        now = k
        cnt = 0
        for minimum, exhausted in route:
            if now >= minimum:
                cnt += 1
                now -= exhausted
            else:
                break
        answer = max(answer, cnt)
            
    return answer