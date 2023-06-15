def solution(picture, k):
    answer = []
    for p in picture:
        temp = ''
        idx = 0
        for i in range(len(p)):
            temp += p[i] * k
        for i in range(k):
            answer.append(temp)
    return answer