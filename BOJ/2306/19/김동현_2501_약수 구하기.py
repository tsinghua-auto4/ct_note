
target, time = map(int, input().split())
counter = 0

iter = 0
while True:
    iter += 1
    if iter > target:
        print(0)
        break

    if target % iter == 0:
        counter += 1
    
    if counter == time:
        print(iter)
        break