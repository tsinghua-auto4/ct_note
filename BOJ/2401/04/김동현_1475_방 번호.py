number = str(input())
data   = [0]*10
for iter in range(len(number)):
    data[int(number[iter])] += 1

tmp = data[6] + data[9]
tmp = tmp//2 + tmp%2

data[6] = 0
data[9] = tmp
print(max(data))