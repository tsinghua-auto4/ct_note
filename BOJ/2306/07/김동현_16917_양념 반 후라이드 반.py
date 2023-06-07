

A, B, C, X, Y = map(int, input().split())

if A+B < C*2:
    print(A*X + B*Y)
else:
    m = min(X, Y)
    print(C*m*2 + min(C*2, A)*max(0,X-m) + min(C*2, B)*max(0, Y-m))