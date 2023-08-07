from collections import deque

N     = int(input())
balloons = deque(enumerate(map(int, input().split())))

ans = []
while balloons:
    idx, delta = balloons.popleft()
    ans.append(idx+1)

    if delta > 0:
        balloons.rotate(-(delta-1))
    elif delta < 0:
        balloons.rotate(-delta)

print(*ans)