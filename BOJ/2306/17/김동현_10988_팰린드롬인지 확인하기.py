def judge(t:str):
    length = len(t)
    for idx in range(length//2):
        if t[idx] != t[length-1-idx]:
            return False
    return True

target = input()
print (1) if judge(target) else print(0)