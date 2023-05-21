import heapq

def solution(operations):
    heap = []
    heapq.heapify(heap)
    for op in operations :
        op_split = op.split()
        if op_split[0]=='I' :
            heapq.heappush(heap,int(op_split[1]))
        else :
            if op_split[1]=='1' and heap:
                heap.pop()
            elif op_split[1]=='-1' and heap:
                heapq.heappop(heap)
    answer = [max(heap) if heap else 0, min(heap) if heap else 0]
    return answer