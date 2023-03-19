import sys

n    = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    nme, kor, eng, mth = map(str, sys.stdin.readline().split())
    data.append((nme, int(kor), int(eng), int(mth)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for cur in data:
    print(cur[0])