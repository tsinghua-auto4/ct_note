
balls = [0, 1, 0, 0]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    balls[a], balls[b] = balls[b], balls[a]

for idx in range(1, 4):
    if balls[idx] == 1:
        print(idx)
        break