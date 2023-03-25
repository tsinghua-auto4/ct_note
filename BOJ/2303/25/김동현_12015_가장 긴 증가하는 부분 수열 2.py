import sys

def bin_search(target, start, end):
    while start <= end:
        mid = (start+end)//2
        if candidate[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

n    = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

candidate = [0]
for cur in data:
    if candidate[-1] < cur:
        candidate.append(cur)
    else:# 크거나 같은 위치(bin_search)에 현재 숫자를 넣어줌, 미래를 위한 전략
        candidate[bin_search(cur, 0, len(candidate)-1)] = cur

print(len(candidate)-1)