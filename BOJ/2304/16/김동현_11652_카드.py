
N = int(input())
check = set()
cards = {}
for _ in range(N):
    card = int(input())
    if card not in check:
        cards[card] = 1
    else:
        cards[card] += 1
    check.add(card)

ans = []
for k in cards:
    ans.append([k, cards[k]])
ans.sort(key = lambda x:(-x[1], x[0]))
print(ans[0][0])