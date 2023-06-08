def solution(brown, yellow):
    answer = []
    all = brown // 2 + 2
    w, h = all, 0
    while w >= h:
        w -= 1
        h += 1        
        if w * h - brown == yellow:
            break
            
    return [w, h]