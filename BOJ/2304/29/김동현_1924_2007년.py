
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

thirtyone = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]

x, y = map(int, input().split())

date = 0
for i in range(1, x):
    if i in thirtyone:
        date += 31
    elif i in thirty:
        date += 30
    else:
        date += 28

date += (y-1)

print(day[date%7])