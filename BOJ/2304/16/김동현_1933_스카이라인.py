# 참고 블로그: https://peisea0830.tistory.com/97

import heapq

# 건물의 개수
N = int(input())

mem, queue  = [], []
height, end = [0]*N, [0]*N
check       = set() # 중복이 없고, 원소 조회는 O(1)

for idx in range(N):
    L, H, R = map(int, input().split())
    
    mem.append([L, idx, 0]) # 왼쪽은 0,
    mem.append([R, idx, 1]) # 오른쪽은 1

    height[idx] = H
    end[idx]    = R

# 메모리에 저장된 높이 포인트들을 (x 위치 -> 왼/오 -> 높이) 순으로 정렬
mem.sort(key= lambda x:(x[0], x[2], -height[x[1]]))


# 현재 높이와 정답을 저장할 변수를 선언하자
cur_height = 0
ans        = []

for i in range(len(mem)):
    x, idx, dir = mem[i]

    # 방향이 왼쪽, 즉 시작점일 때
    if dir == 0:
        # 만약 현재 높이보다 높다면~
        if cur_height < height[idx]:
            cur_height = height[idx]
            ans.append((x, cur_height))
        # 우선순위 큐에 (건물 높이 -> 빨리 끝나는 지점) 순으로 저장
        heapq.heappush(queue, (-height[idx], end[idx]))
    # 끝 점일 때
    else:
        # 지금 건물이 끝났다는 로그 남겨야지, visit 비슷함
        check.add(x)
        # 최대 높이가 끝난 건물이 아닐 때 까지 pop
        while queue:
            if queue[0][1] not in check:
                break
            heapq.heappop(queue)
        # 큐가 비었으면 다 끝나서 높이를 0으로~
        if not queue:
            if cur_height:
                cur_height = 0
                ans.append((x, cur_height))
        # 큐가 안비었으면, 높이가 변하는 지점임
        else:
            if -queue[0][0] != cur_height:
                cur_height = -queue[0][0]
                ans.append((x, cur_height))

for i in range(len(ans)):
    print(ans[i][0], ans[i][1], end=' ')