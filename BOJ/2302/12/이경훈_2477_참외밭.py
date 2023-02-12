import sys
input = sys.stdin.readline

# 입력
k = int(input())
ud = []
lf = []
tt = []

# 방향이 1 혹은 2라면 lf에 3 혹은 4라면 ud에 (인덱스, 방향, 길이) 튜플을 넣는다
for i in range(6):
  dir, m = map(int, input().split())
  if dir == 1 or dir == 2:
    lf.append((i, dir, m))
  else:
    ud.append((i, dir, m))
  tt.append((i, dir, m))

# 좌우 리스트에서 가장 큰 값의 인덱스, 위아래 리스트에서 가장 큰 값의 인덱스를 구해서 큰 사각형의 넓이, 작은 사각형의 넓이를 구한다.
# 가장 큰 값의 양 옆 값의 차가 작은 사각형을 구성한다.
w_idx, *_ = max(lf, key=lambda x:x[2])
h_idx, *_ = max(ud, key=lambda x:x[2])
big_rect = tt[w_idx][2] * tt[h_idx][2]
small_rect = abs(tt[(w_idx+1+6)%6][2] - tt[(w_idx-1+6)%6][2]) * abs(tt[(h_idx+1+6)%6][2] - tt[(h_idx-1+6)%6][2])
ans = big_rect - small_rect
print(k * ans)