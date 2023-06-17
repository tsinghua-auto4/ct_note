
lut = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
        }

total_point = 0
tmp = 0
for _ in range(20):
    _, point, grade = map(str, input().split())
    if grade == 'P':
        continue
    total_point += float(point)
    tmp += lut[grade]*float(point)
print('{:.6f}'.format(tmp/total_point))