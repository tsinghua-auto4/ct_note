import sys

n, k = map(int, sys.stdin.readline().split())

a = 0
b = n
# ab pair 를 k 보다 더 크게 만들자
while a*b < k and b > 0:
    a += 1
    b -= 1

# 예외상황 처리
if k == 0:
    print("B"*n)
    exit(0)
elif b == 0:
    print(-1)
    exit(0)

# while의 ab pair 갯수는 k보다 많아서 1을 빼줘서 b개 작게 만들고, 나머지 모자란 몫을 또 더해줌
remain = k - (a-1)*b
print("A"*(a-1) + "B"*(b-remain) + "A" + "B"*remain)