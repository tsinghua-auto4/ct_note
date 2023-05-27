from itertools import permutations

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if is_prime_number(int("".join(j))):
                answer.add(int("".join(j)))
    return len(answer)