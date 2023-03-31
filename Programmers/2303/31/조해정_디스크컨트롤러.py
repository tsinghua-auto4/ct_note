import heapq


def solution(jobs):
    answer = 0

    jobs.sort()
    n = len(jobs)

    queue = []
    current_time = 0
    cnt = 0
    while cnt < n:
        while jobs:
            if jobs[0][0] > current_time:
                break
            heapq.heappush(queue, jobs.pop(0)[::-1])
        if queue:
            [cost, time] = heapq.heappop(queue)
            current_time += cost
            answer += (current_time - time)
            cnt += 1
        else:
            current_time += 1

    return answer // n
