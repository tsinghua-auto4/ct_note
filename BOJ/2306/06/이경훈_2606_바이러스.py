N = int(input())
num = int(input())
answer = 0
parents = [i for i in range(N+1)]
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if x > y:
            parents[y] = x
        else:
            parents[x] = y

for _ in range(num):
    x, y = map(int, input().split())
    union(x, y)
for i in range(1, N+1):
    find(i)
temp = parents[1]

for i in range(2, N+1):
    if parents[i] == temp:
        answer += 1
print(answer)