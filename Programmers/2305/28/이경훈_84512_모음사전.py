from itertools import product

def solution(word):
    answer = 0
    words = []
    alphabet = ['A','E','I','O','U']
    for i in range(1, 6):
        for candi in product(alphabet, repeat=i):
            words.append(''.join(candi))
    words.sort()
    
    answer = words.index(word) + 1
    
    return answer