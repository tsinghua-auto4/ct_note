def bubbleCounter(start, end):
    global ans, target

    if start < end:
        mid = (start + end)//2
        bubbleCounter(start, mid)
        bubbleCounter(mid+1, end)

        front_idx, back_idx = start, mid+1
        new_target = []

        while front_idx <= mid and back_idx <= end:
            if target[front_idx] <= target[back_idx]:
                new_target.append(target[front_idx])
                front_idx += 1
            else:
                new_target.append(target[back_idx])
                back_idx += 1
                ans += ((mid - front_idx) + 1)
        
        if front_idx <= mid:
            new_target = new_target + target[front_idx : mid+1]
        if back_idx <= end:
            new_target = new_target + target[back_idx : end+1]
        
        for i in range(len(new_target)):
            target[start+i] = new_target[i]

N      = int(input())
target = list(map(int, input().split()))

ans     = 0
bubbleCounter(0, N-1)
print(ans)