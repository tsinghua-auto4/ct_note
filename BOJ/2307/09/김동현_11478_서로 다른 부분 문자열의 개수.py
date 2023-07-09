target = input()
ans    = set()

for length in range(1, len(target)+1):
    for idx in range(0, len(target)-length+1):
        ans.add(target[idx:idx+length])

print(len(ans))