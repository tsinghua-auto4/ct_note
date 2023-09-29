data = list(map(int, input().split()))
a, d = True, True

for iter in range(len(data)-1):
    if a == True and not(data[iter] < data[iter+1]):
        a = False
    if d == True and not(data[iter] > data[iter+1]):
        d= False

if a:
    print("ascending")
elif d:
    print("descending")
else:
    print("mixed")