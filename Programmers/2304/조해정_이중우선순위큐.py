import heapq


def solution(operations):
    answer = []
    minI, maxI = [], []

    for operation in operations:
        [cmd, num_str] = operation.split()
        num = int(num_str)
        if cmd == "I":
            heapq.heappush(minI, num)
            heapq.heappush(maxI, -num)
        elif minI and maxI:
            if num == -1:
                heapq.heappop(minI)
                if not minI or minI[0] > -maxI[0]:
                    minI, maxI = [], []
            else:
                heapq.heappop(maxI)
                if not maxI or -maxI[0] < minI[0]:
                    minI, maxI = [], []

    if not minI or not maxI:
        answer = [0, 0]
    else:
        answer = [-maxI[0], minI[0]]

    return answer
