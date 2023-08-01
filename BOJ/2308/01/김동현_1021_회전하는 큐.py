from collections import deque

N, M    = map(int, input().split())
targets = list(map(int, input().split()))

queue   = deque(list(range(1, N+1)))

cnt = 0
# 모든 대상에 대해 pop
for target in targets:
    # 무한반복
    while True:
        # 제일 앞에 있는 녀석이 타겟이라면 pop
        if queue[0] == target:
            queue.popleft()
            break
        # 아니면 2, 3 번 로직 실행
        else:
            # 내가 찾는 숫자가 전반부에 있다면, 왼쪽회전 -> 찾을 때 까지 반복
            if queue.index(target) < len(queue)/2:
                while queue[0] != target:
                    queue.append(queue.popleft())
                    cnt += 1
            # 내가 찾는 숫자가 후반부에 있다면, 오른쪽회전 -> 찾을 때 까지 반복
            else:
                while queue[0] != target:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)