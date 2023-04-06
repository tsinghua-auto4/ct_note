def solution(n, lost, reserve):
    clothes = [1] * n
    new_lost = sorted(list(set(lost) - set(reserve)))
    new_reserve = list(set(reserve) - set(lost))
    have_extra = dict(zip(new_reserve, [True] * len(new_reserve)))

    for student in new_lost:
        front = student - 1
        back = student + 1
        if front in have_extra:
            have_extra.pop(front)
            continue
        elif back in have_extra and have_extra[back]:
            have_extra.pop(back)
            continue
        clothes[student - 1] = 0

    return sum(clothes)
