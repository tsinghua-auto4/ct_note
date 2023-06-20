
min_x, min_y = 999999999, 999999999
max_x, max_y = -999999999, -999999999

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

if T <= 1:
    print(0)
else:
    print(abs(max_x-min_x)*abs(max_y-min_y))