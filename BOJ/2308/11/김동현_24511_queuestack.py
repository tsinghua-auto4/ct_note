import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque()
for iter in range(N):
    if A[iter] == 0:
        queue.appendleft(B[iter])
if queue == []:
    print(*C)
    sys.exit()

for iter in range(M):
    queue.append(C[iter])
    print(queue.popleft(), end = " ")