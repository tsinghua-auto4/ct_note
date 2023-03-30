import heapq


def solution(scoville, K):
    answer = 0

    scoville.sort()

    part = []
    over_K = False

    for idx, val in enumerate(scoville):
        if val >= K:
            part = scoville[:idx + 1]
            over_K = True
            break

    if not over_K:
        part = scoville[:]

    if len(part) < 2:
        return answer

    while len(part) > 1:
        min1 = heapq.heappop(part)
        min2 = heapq.heappop(part)

        mixed = min1 + 2 * min2
        if mixed < K:
            heapq.heappush(part, mixed)
        elif not over_K:
            heapq.heappush(part, K)
            over_K = True

        answer += 1

    if not part or part[0] >= K:
        return answer

    return -1
