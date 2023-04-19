import sys

input = sys.stdin.readline

n = int(input())
char = {}

for _ in range(n):
    word = input().strip()
    l = len(word)

    for i in range(l, 0, -1):
        char[word[-i]] = char.get(word[-i], 0) + 10**(i-1)

total = 0
nums = [i for i in range(10)]
lst = sorted(char.items(), key=lambda x: -x[1])

for _, val in lst:
    total += (val * nums.pop())

print(total)
