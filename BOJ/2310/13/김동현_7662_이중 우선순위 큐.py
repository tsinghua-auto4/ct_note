import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    pq1 = [] # min heap, 기본
    pq2 = [] # max heap, 내가 만든거
    visit = [False] * 1000001

    # 연산 진행
    for key in range(k):
        op, n = map(str, input().split())
        
        if op == 'I':
            heapq.heappush(pq1, (int(n), key))
            heapq.heappush(pq2, (-int(n), key))
            visit[key] = True #True면 어떠한 힙에서도 삭제되지 않은 상태
        elif n == '1': # 최대값 삭제의 경우
            while pq2 and not visit[pq2[0][1]]: # 최소힙에서 삭제됐지만, 최대힙에선 삭제가 안된 노드를 삭제
                heapq.heappop(pq2)
            if pq2: # 이제 제일 앞에 있는 최대값 노드를 삭제하고, visit에 삭제했다고 갱신함
                visit[pq2[0][1]] = False
                heapq.heappop(pq2)
        else: # 최소값 삭제의 경우
            while pq1 and not visit[pq1[0][1]]: # 최대힙에서 삭제됐지만, 최소힙에선 삭제가 안된 노드를 삭제
                heapq.heappop(pq1)
            if pq1: # 이제 제일 앞에 있는 최소값 노드를 삭제하고, visit에 삭제했다고 갱신함
                visit[pq1[0][1]] = False
                heapq.heappop(pq1)

    # 최소값/최대값 heap 안에서 아직 안지워진 노드를 먼저 삭제하자
    while pq1 and not visit[pq1[0][1]]:
        heapq.heappop(pq1)
    while pq2 and not visit[pq2[0][1]]:
        heapq.heappop(pq2)
    # 최대값/최소값 heap의 길이가 0이 아닐 때, 답안을 출력하자
    if pq1 and pq2:
        print(-pq2[0][0], pq1[0][0])
    else:
        print("EMPTY")