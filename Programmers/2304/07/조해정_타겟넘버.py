def solution(numbers, target):
    answer = 0
    arr = [0]
    dic = {0: 1}

    for n in numbers:
        new_arr = []
        new_dict = {}
        for a in arr:
            plus = a + n
            minus = a - n
            new_arr.append(plus)
            new_arr.append(minus)
            if plus not in new_dict:
                new_dict[plus] = 0
            if minus not in new_dict:
                new_dict[minus] = 0
            new_dict[plus] += dic[a]
            new_dict[minus] += dic[a]
        arr = list(set(new_arr))
        dic = new_dict

    return dic[target]
