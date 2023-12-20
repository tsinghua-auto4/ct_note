while True:
    hist = list(map(int, input().split()))
    if hist[0] == 0:
        break

    stack = []
    ans   = 0

    for i, height in enumerate(hist):
        if i == 0:
            continue

        # 지금 막대기가 스택의 마지막 보다 작으면 최대 직사각형의 면적을 계산함
        if stack and stack[-1][1] > height:
            while stack:  # 스택에서 빼내며 최대 직사각형 면적을 계산
                stack_i, stack_height = stack.pop()
                width_start = 1
                # 아직 스택이 남아있다면, 방금 꺼낸 원소의 높이로 면적계산(스택은 막대기의 높이가 오름차순으로 들어가서 지금 꺼낸 막대기 높이가 최대)
                if stack:
                    width_start = stack[-1][0]+1
                cur = (i - width_start) * stack_height
                ans = max(cur, ans) # 최대값 갱신
                # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
                if not stack or stack[-1][1] <= height:
                    break
        
        # 지금 막대기가 스택의 마지막 보다 크거나 같으면 그냥 추가함, 원래 직사각형의 높이 유지
        if not stack or stack[-1][1] <= height:
            stack.append((i, height))

    # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산
    while stack:
        stack_i, stack_height = stack.pop()
        width_start = 1
        if stack:
            width_start = stack[-1][0]+1
        cur = (hist[0]+1 - width_start) * stack_height
        ans = max(cur, ans) # 최대값 갱신

    print(ans)