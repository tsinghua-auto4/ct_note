def fibonacci(n):
    zeros = [1, 0, 1]
    ones  = [0, 1, 1]
    if n >= 3:
        for i in range(2, n):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(f"{zeros[n]} {ones[n]}")
    
T = int(input())
for _ in range(T):
    target = int(input())
    fibonacci(target)