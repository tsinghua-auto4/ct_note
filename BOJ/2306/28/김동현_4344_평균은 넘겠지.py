
for _ in range(int(input())):
    target  = list(map(float, input().split()))
    average = sum(target[1:])/target[0]
    cnt = 0.0
    for case in target[1:]:
        if case > average:
            cnt += 1
    print("{:.3f}%".format(cnt/target[0]*100))