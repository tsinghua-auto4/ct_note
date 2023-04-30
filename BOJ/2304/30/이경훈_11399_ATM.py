N = int(input())
P = list(map(int, input().split()))
P.sort()
total_sum = 0
sum = 0
for i in range(len(P)):
    sum += P[i]
    total_sum += sum

print(total_sum)
