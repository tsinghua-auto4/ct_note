import sys
input = sys.stdin.readline

# 입력
n = int(input())
data = []

# 재귀함수
# n개의 탑을 이동하는데, _from에서 to로 옮길건데 temp를 보조로 이용함
def hanoi(n, _from, temp, to):
  global cnt
  if n == 1:
    data.append((_from, to))
    return
  hanoi(n-1, _from, to, temp)
  hanoi(1, _from, temp, to)
  hanoi(n-1, temp, _from, to)

# 20 이하의 수만 과정을 보여줌
if n <= 20:
  hanoi(n, 1, 2, 3)
  print(2**n-1)
  for d in data:
    print(*d)
else:
  print(2**n-1)