n, t = map(int, input().split())
data = {}

for iter in range(n):
    pokemon = input()
    data[pokemon] = iter+1
    data[str(iter+1)] = pokemon

for _ in range(t):
    target = input()
    print(data[target])