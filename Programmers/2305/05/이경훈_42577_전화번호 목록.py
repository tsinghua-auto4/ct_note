def solution(pb):
    answer = True
    pb.sort()
    for idx, p in enumerate(pb):
        if idx == 0:
            continue
            
        if pb[idx][0] == pb[idx-1][0]:
            if pb[idx][:len(pb[idx-1])] == pb[idx-1]:
                answer = False
                break
        else:
            continue
    return answer

# 참고할만한 풀이:

1.

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

2. 단 아래 정규식은 시간복잡도가 O(n^2) 이라 효율성 실패

# import re
# def solution(phoneBook):

#     for b in phoneBook:
#         p = re.compile("^"+b)
#         for b2 in phoneBook:
#             if b != b2 and p.match(b2):
#                 return False
#     return True