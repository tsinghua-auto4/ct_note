from heapq import heappush as hpush, heappop as hpop

def solution(jobs):
    tasks = sorted([(job[1], job[0]) for job in jobs], key=lambda x:(x[1], x[0]), reverse=True)
    h = []
    hpush(h, tasks.pop())
    current_time, total_response_time = 0, 0
    while h:
        leng, time = hpop(h)
        current_time = max(current_time + leng, time + leng)
        total_response_time += current_time - time
        while tasks and tasks[-1][1] <= current_time:            
            hpush(h, tasks.pop())
        if tasks and not h:            
            hpush(h, tasks.pop())
    return total_response_time // len(jobs)