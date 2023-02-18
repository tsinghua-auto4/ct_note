import sys
input = sys.stdin.readline

# 입력
x_list, y_list = [], []
ans1, ans2 = 0, 0

# 주어진 세 쌍의 점의 좌표들을 각각 리스트에 넣고 xor연산을 통해 나머지 한 점의 좌표를 구한다.
for _ in range(3):
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)

# ans1 = x_list[0]
# ans2 = y_list[0]

for x in x_list:
  ans1 ^= x

for y in y_list:
  ans2 ^= y

# 출력
print(ans1, ans2)
