while True:
    target = int(input())
    if target == -1:
        break
    stack = []
    for i in range(1, target):
        if target % i == 0:
            stack.append(i)
    if sum(stack) == target:
        print(target, " = ", " + ".join(str(i) for i in stack), sep="")
    else:
        print(target, "is NOT perfect.")