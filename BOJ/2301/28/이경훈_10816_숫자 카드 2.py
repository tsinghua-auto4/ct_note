import sys

input = sys.stdin.readline

# 입력
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards_target = list(map(int, input().split()))
ans = []
card_dic = dict()

# dictionary 만듦
for card in cards:
  if card in card_dic:
    card_dic[card] += 1
  else:
    card_dic[card] = 1

# 만약 딕셔너리에 card_target 키가 있다면 그 밸류 값을 가져오고 없다면 0을 기본 값으로 줌
for card_target in cards_target:
  a = card_dic.get(card_target, 0)
  ans.append(a)

# 출력
print(*ans)
