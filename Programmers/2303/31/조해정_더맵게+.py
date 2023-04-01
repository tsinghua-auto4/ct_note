from collections import deque


def solution(scoville, K):
    answer = 0

    if K == 0:
        return 0

    scoville.sort()
    if scoville[-1] == 0:
        return -1
    elif scoville[0] >= K:
        return 0

    part = deque(scoville)
    # 일단 요소는 무조건 2개 이상이고, mixed는 무조건 하나는 생기는 상황. 아닌 상황은 위에서 이미 거름(line12)
    answer += 1
    min1 = part.popleft()
    min2 = part.popleft()
    mixed = deque([min1 + 2 * min2])

    while len(part) > 1:  # part가 두 개 이상인 동안
        if part[0] >= K:
            part = []
            mixed.append(K)
            break
        answer += 1
        a = mixed[0]
        if len(mixed) == 1:
            b = 1000000001  # 절대 min값으로 선택될 수 없는 값
        else:
            b = mixed[1]
        c, d = part[0], part[1]
        if a < c:
            min1 = mixed.popleft()
            min2 = mixed.popleft() if b < c else part.popleft()
        else:
            min1 = part.popleft()
            min2 = part.popleft() if d < a else mixed.popleft()
        mixed.append(min1 + 2 * min2)

    if len(part) == 1:  # part가 하나 남아있고 그 값이 K보다 적으면 계산에 필요
        part = part[0]
        while mixed:
            if part >= K and mixed[0] >= K:
                break
            if len(mixed) == 1:
                return -1 if (mixed[0] + part) < K else answer + 1
            answer += 1
            min1 = mixed.popleft()
            if part <= min1:
                mixed.append(part + 2 * min1)
                break
            else:
                min2 = mixed.popleft()
                mixed.append(min1 + 2 * min2)

    if len(mixed) == 1:
        return -1 if mixed[0] < K else answer
    while mixed:  # part에 있는 거 다 해치우고, mixed만 고려하면 될 때
        if mixed[0] >= K:
            return answer
        if len(mixed) == 1:
            return -1
        answer += 1
        min1 = mixed.popleft()
        min2 = mixed.popleft()
        mixed.append(min1 + 2 * min2)

    return answer
