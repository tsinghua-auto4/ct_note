def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''
        digit_flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                digit_flag = True
                number += file[i]
            elif not digit_flag:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))
        
    answer.sort(key = lambda x:(x[0].upper(), int(x[1])))
    return [''.join(t) for t in answer]