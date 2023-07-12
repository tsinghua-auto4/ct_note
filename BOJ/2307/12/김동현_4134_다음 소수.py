
def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    cur = int(input())
    while True:
        if cur == 0 or cur == 1:
            print(2)
            break
        
        elif check(cur):
            print(cur)
            break

        else:
            cur += 1