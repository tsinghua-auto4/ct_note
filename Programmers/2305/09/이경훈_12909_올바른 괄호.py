def solution(ss):
    answer = True
    stk = []
    for s in ss:
        if s == '(':
            stk.append(s)
        else:
            if not stk or stk[-1] != '(':
                return False
            stk.pop()
    if stk:
        return False
    return True