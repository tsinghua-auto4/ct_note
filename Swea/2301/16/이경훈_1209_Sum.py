for t in range(10):
  tc = int(input())
  data = [list(map(int, input().split())) for _ in range(100)]
  
  max = 0
  
  for r in range(100):
    sum = 0
    for c in range(100):
      sum += data[r][c]
    if sum > max:
      max = sum

  for c in range(100):
    sum = 0
    for r in range(100):
      sum += data[r][c]
    if sum > max:
      max = sum
      
  sum1 = 0
  sum2 = 0
  
  for r in range(100):
    sum1 += data[r][r]  
  if sum1 > max:
    max = sum1

  for r in range(100):
    sum2 += data[r][99-r]  
  if sum2 > max:
    max = sum2
    
  print(f'#{tc} {max}')