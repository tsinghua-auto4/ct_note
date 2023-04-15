import re

candidate = []
p = re.compile("[a-z]")

for _ in range(int(input())):
    cur = input().rstrip()
    tmp = p.sub(' ', cur).split()
    
    for t in tmp:
        candidate.append(int(t))

candidate.sort()
for cur in candidate:
    print(cur)