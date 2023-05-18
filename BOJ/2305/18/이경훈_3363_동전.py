import sys
input = sys.stdin.readline

def check(fake_coin: str, symbol: str, commands: list):
    sign = ('=', '>', '<') if symbol == '+' else ('=', '<', '>')

    for command in commands:
        test = 0
        if fake_coin in command[:4]:
            test = 1
        elif fake_coin in command[5:]:
            test = 2
        if command[4] != sign[test]:
            return False
    return True


commands = []
for _ in range(3):
    temp = input().split()
    if not temp:
        temp = input().split()
    commands.append(temp)

answer = []
for i in map(str, range(1, 13)):
    for symbol in ('+', '-'):
        if check(i, symbol, commands):
            answer.append(i + symbol)

if not answer:
    print('impossible')
elif len(answer) > 1:
    print('indefinite')
else:
    print(*answer)