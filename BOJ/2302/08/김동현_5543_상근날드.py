import sys

def solution():
    price = []
    for _ in range(5):
        price.append(int(sys.stdin.readline().rstrip()))
    burger = min(price[0:3])
    drink = min(price[3:5])
    print(burger + drink - 50)

solution()