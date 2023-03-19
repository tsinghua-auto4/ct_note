import sys
import heapq # 힙, python 제공 최소힙, 복잡도는 O(logN)

n, k = map(int,sys.stdin.readline().split())
gems = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

gems.sort() # 무게/가격 오름차순(무게 우선) 
bags.sort() # 가방 무게 오름차순

ans = 0     # 결과 출력값 초기화
greedy = [] # greedy 보석의 가격 저장

for bag in bags:
    while gems and gems[0][0] <= bag:       # bag에 넣을 수 있는 보석일 때
        heapq.heappush(greedy, -gems[0][1]) # 가격을 힙에 저장(음수로 저장하여 최소힙을 최대힙으로), python heapq는 최소힙임
        heapq.heappop(gems)                 # 가격 저장한 보석은 버리기
    if greedy: #bag 무게 이하 보석 가격 다 저장했으면
        ans -= heapq.heappop(greedy) # 제일 가치가 높은 가격 고르기, 남는 보석은 다음 bag에 넣을 수 있음
print(ans)