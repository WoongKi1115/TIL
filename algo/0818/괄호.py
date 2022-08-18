T = int(input())
for tc in range(1, T+1):
    problem = input()
    stack = []
    result = 1
    for c in problem:
        if c == '{' or c == '(':
            stack.append(c)
        if c == '}' or c ==')':
            if len(stack) == 0:
                result = 0
                break
            bracket = stack.pop()
            if not ((bracket == '(' and c == ')') or (bracket == '{' and c == '}')):
                result = 0
                break

    if len(stack) > 0:
        result = 0
    print(f"#{tc} {result}")
