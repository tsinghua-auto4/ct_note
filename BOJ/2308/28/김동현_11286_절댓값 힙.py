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
            _, ans = heapq.heappop(queue)
            sys.stdout.writelines(str(ans)+'\n')
    else:
        heapq.heappush(queue, (abs(cur), cur))