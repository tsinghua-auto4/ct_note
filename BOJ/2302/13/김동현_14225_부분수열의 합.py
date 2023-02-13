import sys
from itertools import combinations


if __name__ == "__main__":
    n    = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    ans  = []

    for i in range(n):
        tmp = combinations(data, i+1)
        for cur in tmp:
            t = 0
            for c in cur:
                t += c
            ans.append(t)
    val_max = max(ans)
    conv    = set(ans)
    
    for i in range(1, val_max+1):
        if i not in conv:
            print(i)
            exit()
    print(val_max+1)
