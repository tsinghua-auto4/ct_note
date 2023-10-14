import heapq

N = int(input())
dasom = int(input())

heap = []
for _ in range(N-1):
    num = int(input())
    heapq.heappush(heap, (-num, num))

if len(heap) == 0:
    print(0)

else:
    cnt = 0
    while True:
        cur = heapq.heappop(heap)[1]
        if cur >= dasom:
            cnt += 1
            dasom += 1
            heapq.heappush(heap, (-cur+1, cur-1))
        else:
            break

    print(cnt)