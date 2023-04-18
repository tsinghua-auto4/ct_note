N, k = map(int, input().split())

ans   = 0 # 답안
digit = 1 # 몇 자리 수~
unit  = 9 # 지금 자리 수의 숫자는 숫자당 unit 개~

# k가 0 보다 작을 때 까지 지금 자리 수의 길이 만큼 빼주자~
# 지금 자리 수의 길이: (규칙이 보이는가?!)
# -> 한자리는 1~9 총 9개
# -> 두자리는 10~99 총 90*2개
# -> 세자리는 100~999 총 900*3개
while k > digit*unit:
    k     -= digit*unit
    ans   += unit
    digit += 1
    unit  *= 10

# 남은 k를 ans에서 차이를 보상해주자
# ans+1 -> 다음 자리 수~ (ex. 2자리수 -> 3자리수 scale up!)
# (k-1)//digit -> target 숫자
ans = (ans+1) + (k-1)//digit

# 형식에 맞게 답안 출력
if ans > N:
    print(-1)
else:
    # (k-1)//digit으로 target 숫자에 왔으니, %로 정확한 위치를 지정
    print(str(ans)[(k-1)%digit])
