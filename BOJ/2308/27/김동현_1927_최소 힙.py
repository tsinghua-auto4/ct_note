import sys
import heapq

N = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(N):
    cur = int(sys.stdin.readline().rstrip())
    if cur == 0:
        if len(queue) == 0:
            sys.stdout.writelines('0'+'\n')
        else:
            sys.stdout.writelines(str(heapq.heappop(queue))+'\n')
    else:
        heapq.heappush(queue, cur)