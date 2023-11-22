while True:
    loop = int(input())
    if loop == 0:
        break
    line = '*'
    for _ in range(loop):
        print(line)
        line += '*'