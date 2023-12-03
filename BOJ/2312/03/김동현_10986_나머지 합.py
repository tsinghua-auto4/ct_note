N, M = map(int, input().split())
data = list(map(int, input().split()))

sum = 0
numRemainder = [0] * M

for i in range(N):
    sum += data[i]
    numRemainder[sum % M] += 1

result = numRemainder[0]

for i in numRemainder:
    result += i*(i-1)//2

print(result)