import sys

target = sys.stdin.readline().rstrip()
answer = ''

for cur in target:
    if cur.isupper():
        answer += cur.lower()
    else:
        answer += cur.upper()

print(answer)