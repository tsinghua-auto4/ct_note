def solution(name):
    answer = 0
    change = [min(ord(n) - ord('A'), 26 - (ord(n) - ord('A'))) for n in name]
    l = len(name)
    min_val = l - 1

    for i, c in enumerate(name):
        next_i = i+1
        while next_i < l and name[next_i] == 'A':
            next_i += 1
        min_val = min(min_val, i*2 + l - next_i, i + 2*(l - next_i))    
    answer = sum(change) + min_val
    
    return answer