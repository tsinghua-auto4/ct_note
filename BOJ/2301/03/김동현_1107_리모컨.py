import sys

input = sys.stdin.readline

def solution():
    target = int(input())
    n      = int(input())
    broken = list(map(int, input().split()))

    min_count = abs(100 - target)

    for nums in range(1000001):
        nums = str(nums)

        for j in range(len(nums)):
            if int(nums[j]) in broken:
                break
            elif j == len(nums) - 1:
                min_count = min(min_count, len(nums) + abs(target - int(nums)))

    print(min_count)

solution()