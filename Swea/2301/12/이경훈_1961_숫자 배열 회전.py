T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  square = [list(input().split()) for _ in range(n)]
  
  list1, list2, list3 = [], [], []
  
  for c in range(n): # 90도 회전했을 때
    temp = ""
    for r in range(n-1, -1, -1):
      temp += square[r][c]
    list1.append(temp)

  for r in range(n-1, -1, -1): # 180도 회전했을 때
    temp = ""
    for c in range(n-1, -1, -1):
      temp += square[r][c]
    list2.append(temp)

  for c in range(n-1, -1, -1): # 270도 회전했을 때
    temp = ""
    for r in range(n):
      temp += square[r][c]
    list3.append(temp)
  
  print(f'#{test_case}')
  for pair in zip(list1, list2, list3):
    print(*pair)