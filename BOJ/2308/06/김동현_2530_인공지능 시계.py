h, m, s = map(int, input().split())
time    = int(input())

s += time

m += s//60
s %= 60

h += m//60
m %= 60

h %= 24

print(h, m, s)