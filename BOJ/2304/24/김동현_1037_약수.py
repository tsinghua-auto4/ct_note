
quantity = int(input())
divisor  = list(map(int, input().split()))

div_max = max(divisor)
div_min = min(divisor)

print(div_max*div_min)