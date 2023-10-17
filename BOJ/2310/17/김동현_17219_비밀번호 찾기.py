N, M = map(int, input().split())
LUT  = {}
for _ in range(N):
    site, pw = map(str, input().split())
    LUT[site] = pw

for _ in range(M):
    site = input()
    print(LUT[site])