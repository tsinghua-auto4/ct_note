
stack = [0]
while True:
    cur = input()
    if cur == '.':
        break
    for c in cur:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)

    if len(stack) == 1:
        print("yes")
    else:
        print("no")
    
    stack = [0]