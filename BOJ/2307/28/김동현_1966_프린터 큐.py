from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    tar  = deque(list(map(int, input().split())))
    
    cnt = 0
    while True:
        prio = max(tar)
        cur = tar.popleft()
        M -= 1
        if cur == prio:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            tar.append(cur)
            if M < 0:
                M = len(tar) -1 