S = int(input())
N = 1

while N*(N+1)//2 <= S:
    N += 1

print(N-1)