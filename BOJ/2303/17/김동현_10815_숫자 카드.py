import sys

def solution(array, target, start, end): #binary_search
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n     = int(sys.stdin.readline())
card  = list(map(int, sys.stdin.readline().split()))
m     = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

for i in range(m):
    if solution(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')