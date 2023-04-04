def solution(brown, yellow):
    total = brown + yellow
    answer = [yellow + 2, 3]

    for h in range(2, yellow + 1):
        w = yellow // h
        if w * h == yellow and (w + 2) * (h + 2) == total:
            answer = sorted([w + 2, h + 2], reverse=True)
            break

    return answer
