import re

N = int(input())

pre, post = map(str, input().split('*'))
pattern   = re.compile(pre + ".*" + post + "+")

for _ in range(N):
    cur = str(input())
    res = pattern.search(cur)
    if res and res.group() == cur:
        print("DA")
    else:
        print("NE")