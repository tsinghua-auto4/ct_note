from itertools import permutations


N         = int(input())
numbers   = list(map(int, input().split()))
operators = list(map(int, input().split()))

operator = '+' * operators[0] + '-' * operators[1] + '*' * operators[2] + '/' * operators[3]
cases    = permutations(operator, N-1)

max_result = float('-inf')
min_result = float('inf')

for case in cases:
    result = numbers[0]
    for i in range(1, N):
        if case[i-1] == '+':
            result += numbers[i]
        elif case[i-1] == '-':
            result -= numbers[i]
        elif case[i-1] == '*':
            result *= numbers[i]
        elif case[i-1] == '/':
            if result < 0 and numbers[i] > 0: 
                result = -1*( result*(-1) // numbers[i])
            else:
                result //= numbers[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)