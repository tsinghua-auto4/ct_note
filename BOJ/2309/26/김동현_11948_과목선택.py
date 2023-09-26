ans = 0
data1 = []
data2 = []
for _ in range(4):
    data1.append(int(input()))
for _ in range(2):
    data2.append(int(input()))
data1.sort()
data2.sort()
ans = sum(data1[1:]) + data2[1]
print(ans)