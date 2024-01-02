## https://zynar.tistory.com/276 간결한 코드, 참고해서 외우자 그냥


import sys

u, n = map(int, sys.stdin.readline().split())
people_dict = dict()

for _ in range(n):
    s, p = sys.stdin.readline().split()
    if int(p) <= u:
        people_dict[p] = people_dict.get(p, list()) + [s]

min_count = min([len(i) for i in people_dict.values()])
min_key = min([int(i) for i in people_dict.keys() if len(people_dict[i]) == min_count])

print(people_dict[str(min_key)][0], min_key)