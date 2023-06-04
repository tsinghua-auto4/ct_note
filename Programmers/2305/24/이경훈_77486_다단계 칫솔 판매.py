def solution(enroll, referral, seller, amount):
    answer = []
    relationship = {e : r for e, r in zip(enroll, referral)}
    money = {e : 0 for e in enroll}
    
    for s, a in zip(seller, amount):
        profit = a * 100
        while s != '-':
            money[s] += profit - int(profit * 0.1)
            s = relationship[s]
            profit = int(profit * 0.1)
            if profit == 0:
                break
    
    for e in enroll:
        answer.append(money[e])
        
    return answer