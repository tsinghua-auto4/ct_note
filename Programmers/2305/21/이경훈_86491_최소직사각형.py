def solution(sizes):
    answer = 0
    X, Y = [], []
    for x, y in sizes:
        if x < y:
            x, y = y, x
        X.append(x)
        Y.append(y)
    answer = max(X)* max(Y)
        
    return answer