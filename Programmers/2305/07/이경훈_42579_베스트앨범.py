def solution(gs, ps):
    list = []
    total = {}
    genre = {}
    
    for idx, g in enumerate(gs):
        if g in total:
            total[g] += ps[idx]
            genre[g].append((ps[idx], idx))
        else:
            total[g] = ps[idx]
            genre[g] = []
            genre[g].append((ps[idx], idx))
    
    for g, _ in sorted(total.items(), key = lambda x : -x[1]):
        for val, i in sorted(genre[g], key = lambda x: -x[0])[:2]:
            list.append(i)    
    
    return list