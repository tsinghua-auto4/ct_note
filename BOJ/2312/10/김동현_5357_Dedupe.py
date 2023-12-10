for _ in range(int(input())):
    target = input()
    ans = ""
    for iter in range(len(target)):
        if len(ans) == 0 or len(ans) > 0 and ans[-1] != target[iter]:
            ans += target[iter]
    print(ans)