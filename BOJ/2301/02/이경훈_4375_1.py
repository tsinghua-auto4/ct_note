import sys, math

input = sys.stdin.readline

while True: # 테스트케이스의 수가 정해지지 않았기에 EoF가 뜰 때까지 반복
  
  try: # EoF 에러가 발생하지 않으면
    n = int(input())
    temp = 1 # 1로만 이루어진 수, 가장 작은 1부터 시작
    
    while True:
      if temp % n == 0: 
        answer = temp
        break
      else: # n으로 나눠떨어지지 않으면 다음 후보 준비
        temp *= 10
        temp += 1
    print(int(math.log10(answer))+1) # 몇자리 수인지 알기 위해서 밑이 10인 로그를 취하고 정수 부분을 구한다
    
  except:
    break