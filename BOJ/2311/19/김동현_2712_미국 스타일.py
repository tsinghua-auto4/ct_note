number = {'kg': 2.2046, 'lb': 0.4536, 'l': 0.2642, 'g': 3.7854}
units  = {'kg': 'lb', 'lb': 'kg', 'l': 'g', 'g': 'l'}

T = int(input())
for _ in range(T):
    a, b = map(str, input().split())

    print("%.4f %s" %(float(a)*number[b], units[b]))