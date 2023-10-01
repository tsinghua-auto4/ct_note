while True:
    cur = input()
    if cur == '0':
        break
    flag = True
    for iter in range(len(cur)//2):
        if cur[iter] != cur[len(cur)-1-iter]:
            flag = False
            break
    if not flag:
        print("no")
    else:
        print("yes")