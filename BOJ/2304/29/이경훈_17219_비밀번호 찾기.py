N, M = map(int, input().split())

info = dict()

site = []

for _ in range(N):
    site_name, pw = input().split()
    info[site_name] = pw

for _ in range(M):
    print(info[input()])
