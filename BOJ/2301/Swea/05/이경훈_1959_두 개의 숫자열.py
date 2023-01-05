t = int(input())
for test_case in range(t):
  sum = 0
  tmp = 0
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  if n >= m: # 숫자열 A의 길이가 숫자열 B의 길이보다 길거나 같으면
    for i in range(n-m+1):
      for j in range(m):
        tmp += a[i+j] * b[j] # 짧은 숫자열 B을 기준으로 함
      if tmp > sum: # 이때 그 전의 합보다 크다면
        sum = tmp # 대체
      tmp = 0
  else: # 위와 반대
    for i in range(m-n+1):
      for j in range(n):
        tmp += a[j] * b[i+j]
      if tmp > sum:
        sum = tmp
      tmp = 0

  print("#"+str(test_case+1), sum)
