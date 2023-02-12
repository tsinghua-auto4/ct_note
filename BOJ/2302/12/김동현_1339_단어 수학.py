import sys

if __name__ == "__main__":
    n     =int(sys.stdin.readline())
    words = []
    alloc = {}
    for _ in range(n):
        words.append(sys.stdin.readline().rstrip())

    for word in words:
        square_root = len(word) - 1
        for c in word:
            if c in alloc:
                alloc[c] += pow(10, square_root)
            else:
                alloc[c] = pow(10, square_root)
            square_root -= 1 

    alloc = sorted(alloc.values(), reverse=True)

    result,m = 0,9
    for value in alloc:
        result += value * m
        m -= 1

    print(result)