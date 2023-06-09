from itertools import combinations_with_replacement

n   = int(input())
lut = [1, 5, 10, 50]
mem = []

for tmp in combinations_with_replacement(range(4), n):
    sum = 0
    for idx in tmp:
        sum += lut[idx]
    mem.append(sum)
print(len(set(mem)))