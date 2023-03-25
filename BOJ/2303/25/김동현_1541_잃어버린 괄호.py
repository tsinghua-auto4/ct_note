import sys

target = str(sys.stdin.readline().rstrip())
data   = list(map(int, target.replace('-', ' ').replace('+', ' ').split()))
stack  = []
for cur in target:
    if cur == '-' or cur == '+':
        stack.append(cur)

idx = 1
while idx < len(stack):
    if stack and stack[idx - 1] == '-':
        stack[idx] = '-'
    idx += 1

if data:
    ans = data[0]
    for i in range(1, len(data)):
        if stack[i-1] == '-':
            ans -= data[i]
        else:
            ans += data[i]
    print(ans)