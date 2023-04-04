import itertools


def solution(numbers):
    answer = 0

    numbers = list(numbers)
    permutations = []

    for i in range(len(numbers)):
        permutation = itertools.permutations(numbers, i + 1)
        permutation = list(map(lambda x: int(''.join(x)), permutation))
        permutations.extend(permutation)

    permutations = list(set(permutations))

    for p in permutations:
        if p < 2:
            continue
        is_Prime = True
        for i in range(2, int(p ** 0.5 + 1)):
            if p % i == 0:
                is_Prime = False
                break
        if is_Prime:
            answer += 1

    return answer
