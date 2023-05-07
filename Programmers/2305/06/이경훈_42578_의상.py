from collections import Counter

def solution(cs):
    answer = 1
    species = Counter(kind for _, kind in cs)
    for v in species.values():
        answer *= (v+1)
    return answer-1