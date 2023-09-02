N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for cur in B:
    print(1) if cur in A else print(0)