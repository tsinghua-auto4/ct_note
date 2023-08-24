a, b, c = map(int, input().split())
ans = a*b-c
print(ans if ans >= 0 else 0)