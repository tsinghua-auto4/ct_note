def solution(arr):
    lst, stack = [0], [0]

    for i in range(len(arr) - 1, -1, -1):
        if i % 2 == 0:
            # 숫자이면 리스트에 더해준다
            # a - b + c + d + e이면, 일단 b까지 계산해보면... lst = [0, 0+e, 0+e+d, 0+e+d+c, 0+e+d+c+b], 나중에 저 0 위치에 경우의 수 넣어줄 것
            lst.append(int(arr[i]) + (lst[-1] if lst else 0))
            continue

        if arr[i] == "-":  # - 부호 뒤로 경우 따져서 구해서 + 로 바꿔주기
            # 어차피 {-lst[-1] - s}와 {2 * lst[j] + s - lst[-1]}만 보는데, s가 저번 연산으로 나온 경우의 수고 나머지는 모두 상수이니,
            # 상수 제거하면 {-s} 와 {+s}가 경우로 더해지는 것을 알 수 있다. 그럼 저번 경우에서 제일 큰 값과 제일 작은 값만 보면 되니까 그렇게 해줌
            max_stack, min_stack = -987654321, 987654321
            for s in stack:
                # last는 "-" 부호 뒤를 모두 괄호로 감쌌을 때 나오는 더하기 값
                # 예) 1 - a + b + c + d의 경우 1-(a+b+c+d) = 1-last
                last = lst[-1] + s
                max_stack = max(max_stack, -last)
                min_stack = min(min_stack, -last)
                for j in range(len(lst) - 1):
                    num = 2 * lst[j] + s - lst[-1]      # 2 * lst[j] + 2 * s - last  => -sum(전체괄호) + 2*(부분괄호 제외된 값들 합)
                    max_stack = max(max_stack, num)
                    min_stack = min(min_stack, num)

            stack = [max_stack, min_stack]
            lst = [0]  # 리스트 비워두는 거 잊지 않기

    return lst[-1] + max(stack)