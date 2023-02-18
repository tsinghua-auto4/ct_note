import sys
input = sys.stdin.readline

while True:  
  data = list(map(int, input().split()))
  # 0, 0, 0이 들어오면 종료
  if(data[0] == 0 and data[1] == 0 and data[2] == 0):
    break    
  # 정렬
  data.sort()

  # 피타고라스의 정의 사용
  if(data[0]**2 + data[1]**2 == data[2]**2):
    print('right')
  else:
    print('wrong')
