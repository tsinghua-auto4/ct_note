_x = []
_y = []

for _ in range(3):
    cx, cy = map(int, input().split())
    _x.append(cx)
    _y.append(cy)

ax, ay = -1, -1
for idx in range(3):
    if _x.count(_x[idx]) == 1:
        ax = _x[idx]
    if _y.count(_y[idx]) == 1:
        ay = _y[idx]
print(ax, ay)