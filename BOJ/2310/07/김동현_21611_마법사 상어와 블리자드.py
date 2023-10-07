from collections import deque

def indexing():
    global n, graph
    nr, nc = n//2, n//2
    move   = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    depth  = 0

    while True:
        for dir in range(4):
            if dir%2 == 0:
                depth += 1
            for _ in range(depth):
                dr, dc = move[dir]
                nr, nc = nr+dr, nc+dc
                graphIdx.append((nr, nc))
                if nr == 0 and nc == 0:
                    return

def blizzard(d, s):
    global n, graph
    cr, cc = n//2, n//2
    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dr, dc = direction[d]

    for iter in range(1, s+1):
        nr, nc = cr+dr*iter, cc+dc*iter
        if not(0 <= nr < n and 0 <= nc < n):
            break
        graph[nr][nc] = 0

def fill_blank():
    blankIdx = deque()
    for r, c in graphIdx:
        if graph[r][c] == 0:
            blankIdx.append((r, c))
        elif graph[r][c] > 0 and blankIdx:
            pr, pc = blankIdx.popleft()
            graph[pr][pc] = graph[r][c]
            graph[r][c] = 0
            blankIdx.append((r, c))

def bomb():
    visited = deque()
    cnt = 0
    num = -1
    flag = False
    for r, c in graphIdx:
        if num == graph[r][c]:
            visited.append((r, c))
            cnt += 1
        else:
            if cnt >= 4:
                score[num-1] += cnt
                flag = True

            while visited:
                nr, nc = visited.popleft()
                if cnt >= 4:
                    graph[nr][nc] = 0

            num = graph[r][c]
            cnt = 1
            visited.append((r, c))

    return flag

def grouping():
    cnt = 1
    tr, tc = graphIdx[0]
    num  = graph[tr][tc]
    nums = []

    for idx in range(1, len(graphIdx)):
        r, c = graphIdx[idx]
        if num == graph[r][c]:
            cnt += 1
        else:
            nums.append(cnt)
            nums.append(num)
            num = graph[r][c]
            cnt = 1

    idx = 0
    for r, c in graphIdx:
        if not nums:
            break
        graph[r][c] = nums[idx]
        idx += 1
        if idx == len(nums):
            break


n, m  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

score = [0, 0, 0]
graphIdx = deque()
indexing()

# 이제 m 번의 블리자드 스킬을 써보자
for _ in range(m):
    # 1. 블리자드 스킬의 방향과 거리를 입력받자
    d, s = map(int, input().split())
    
    # 2. 블리자드 스킬로 필드에 구슬을 없애보자
    blizzard(d-1, s)

    # 3. 구슬이 없어진 자리를 옆에 있는 구슬로 채우자(땡겨주는 함수)
    fill_blank()
    # 4. 땡겨진 필드에 같은 종류의 구슬이 4개 이상 붙어있다면 터뜨리자
    while bomb():
        # 5. 구슬이 없어진 자리를 옆에 있는 구슬로 채우자(땡겨주는 함수)
        fill_blank()
    # 6. 구슬을 변화하자 A,B
    grouping()

ans = 0
for iter in range(3):
    ans += (iter+1) * score[iter]
print(ans)