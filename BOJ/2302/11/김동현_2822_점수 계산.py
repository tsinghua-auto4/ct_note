import sys

def solution():
    raw = []
    for _ in range(8):
        raw.append(int(sys.stdin.readline()))

    sorted = raw.copy()
    sorted.sort()
    third = sorted[2]

    total = 0
    ans = []
    for i in range(8):
        if raw[i] > third:
            total += raw[i] 
            ans.append(i+1)

    print(total)
    print(*ans)


solution()