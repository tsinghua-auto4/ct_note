minkook = list(map(int, input().split()))
mansae  = list(map(int, input().split()))

if sum(minkook) >= sum(mansae):
    print(sum(minkook))
else:
    print(sum(mansae))