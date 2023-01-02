a, b = map(int, input().split())

def getGcd(a, b): # 유클리드 호제법 사용해서 최대공약수 구하기
  if b == 0:
    return a
  return getGcd(b, a%b) # a와 b의 최대공약수는 b와 a%b의 최대공약수와 같다는 성질을 이용!

def getLcm(a, b): # 최소 공배수 구하기
  return a * b // getGcd(a, b) # a를 g*a' b를 g*b'로 보면 결국 최소공배수인 ga'b'는 a*b//g 를 통해 구할 수 있다

print(getGcd(a, b))
print(getLcm(a, b))