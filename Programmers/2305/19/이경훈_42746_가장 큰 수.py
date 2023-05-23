def solution(numbers):
    answer = ''
    numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x: 3*x)
    answer = "".join(numbers)
    return '0' if answer[0] == '0' else answer