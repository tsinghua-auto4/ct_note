t = int(input())
for tc in range(1, t+1):
  input() # 맨 처음 쓸데 없는 값 제거
  data = list(map(int, input().split()))
  dic = dict() # 딕셔너리 선언
  for d in data:
    if d in dic: # 이미 있는 값이면
      dic[d] += 1 # 1추가
    else: # 없으면
      dic[d] = 1 # 생성
  max_val = 0 # 딕셔너리의 밸류값
  max_key = 0 # 딕셔너리의 키값
  sorted_dic = sorted(dic.items(), key = lambda item: (item[1], item[0]), reverse = True) # 내림차순 정렬
  print(f'#{tc} {sorted_dic[0][0]}')