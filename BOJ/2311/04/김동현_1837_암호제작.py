import math

P, K = map(int, input().split())

mem = []
for iter in range(2, K):
    prime = True
    for i in range(2, int(math.sqrt(iter))+1):
        if iter%i == 0:
            prime = False
            break
    if prime:
        mem.append(iter)

for iter in mem:
    if P%iter == 0:
        print("BAD {}".format(iter))
        exit()
print("GOOD")