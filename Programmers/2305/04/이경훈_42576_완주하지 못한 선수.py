# import collections 

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

## 위의 풀이는 간단하나 시간이 더 오래 걸림

## 나의 플이 :
def solution(ps, cs):
    answer = ''
    p_dict = dict()
    c_dict = dict()
    for p in ps:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
    for c in cs:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1

    for p in ps:
        if p_dict[p] != c_dict.get(p):
            answer = p
            break

    return answer