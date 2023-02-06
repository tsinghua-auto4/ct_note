from collections import deque

def solution(A):
    
    # 피보나치 수열 셋팅
    target = len(A)
    if target == 0:
        return 1

    fibo = [0, 1]
    while True:
        n = fibo[-1] + fibo[-2]
        if n > target+1:
            break
        fibo.append(n)
    #print(fibo)

    fibo.sort(reverse=True)
    ret = -1
    arrived = False
    q = deque()
    q.append((-1, 0))
    visit = [False] * (target + 1)
    while q:
        pos, cnt = q.popleft()
        # print(pos, cnt)
        
        if arrived:
            break

        for f in fibo:
            next_pos = pos + f

            if next_pos == target:
                arrived = True
                ret = cnt + 1
                break

            if next_pos < target and not visit[next_pos] and A[next_pos] == 1:
                q.append((next_pos, cnt + 1))
                visit[next_pos] = True
    
    return ret