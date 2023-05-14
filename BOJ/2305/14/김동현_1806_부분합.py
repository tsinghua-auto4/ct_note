import sys

N, S = map(int, input().split())
data = list(map(int, input().split()))

lft, rgt = 0, 0
ans = sys.maxsize
tmp = 0

while True:
    if tmp >= S: # 총 합이 S가 넘으면, lft를 우측으로 이동해서 수를 줄여보자
        ans = min(ans, rgt-lft)
        tmp -= data[lft]
        lft += 1
    elif rgt == N: # 옮긴 rgt 포인터가 범위 밖으로 벗어났다면, 끝임
        break
    else: # 총 합이 S가 안되면, rgt를 우측으로 이동해서 수를 늘려보자
        tmp += data[rgt]
        rgt += 1


ans = ans if ans != sys.maxsize else 0
print(ans)