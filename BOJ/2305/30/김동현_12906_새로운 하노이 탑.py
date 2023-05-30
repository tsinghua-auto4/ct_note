import sys
from collections import deque

def judge(a: str, b: str, c: str):
    if 'B' in a or 'C' in a:
        return False
    if 'A' in b or 'C' in b:
        return False
    if 'A' in c or 'B' in c:
        return False
    return True

def solution(stack: list):
    visit = set()
    
    queue = deque([(*stack, 0)])
    while queue:
        stack_a, stack_b, stack_c, step = queue.popleft()

        if judge(stack_a, stack_b, stack_c):
            return step
        
        case = stack_a + '/' + stack_b + '/' + stack_c
        if case not in visit:
            visit.add(case)
            if len(stack_a) > 0:
                queue.append((stack_a[:-1], stack_b + stack_a[-1], stack_c, step+1))
                queue.append((stack_a[:-1], stack_b, stack_c + stack_a[-1], step+1))
            if len(stack_b) > 0:
                queue.append((stack_a, stack_b[:-1], stack_c + stack_b[-1], step+1))
                queue.append((stack_a + stack_b[-1], stack_b[:-1], stack_c, step+1))
            if len(stack_c) > 0:
                queue.append((stack_a, stack_b + stack_c[-1], stack_c[:-1], step+1))
                queue.append((stack_a + stack_c[-1], stack_b, stack_c[:-1], step+1))


towers = [sys.stdin.readline().strip()[2:] for _ in range(3)]
print(solution(towers))