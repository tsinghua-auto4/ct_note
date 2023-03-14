N = int(input())
N //= 4
list = []
for _ in range(N):
  list.append('long')

list.append('int')

print(" ".join(list))