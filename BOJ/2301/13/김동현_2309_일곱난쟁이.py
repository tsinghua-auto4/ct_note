import sys
from itertools import combinations


def solution():

    data = [int(sys.stdin.readline()) for _ in range(9)]

    for i in combinations(data, 7):
        if sum(i) == 100:
            for j in sorted(i):
                print(j)
            break


solution()