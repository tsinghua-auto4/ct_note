
N = int(input())
A = []
# 수의 규칙, max(sort 후 위치 - 원래 위치) == max bubble 횟수
for i in range(N):
    A.append((int(input()), i))

A.sort(key = lambda x:x[0])

# 여기서 문제가 원하는 max bubble 횟수 + 1 해서 출력하자
ans = -float('inf')
for i in range(N):
    ans = max(ans, (A[i][1]-i) + 1)

print(ans)