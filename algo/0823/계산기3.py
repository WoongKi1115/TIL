T = 10
for tc in range(1, T + 1):
    N = int(input())
    problem = input()
    stack = []
    new = ''
    icp = {'+': 1, '*': 2, '(': 3}
    isp = {'+': 1, '*': 2, '(': 0}

    for i in range(N):
        if '0' <= problem[i] <= '9':
            new += problem[i]
        elif problem[i] == ')':
            while stack[-1] != '(':
                new+=stack.pop()
            stack.pop()
        else:
            if stack:
                while icp[problem[i]] <= isp[stack[-1]]:
                    new+=stack.pop()
                    if not stack:
                        break
            stack.append(problem[i])
    while stack:
        new+=stack.pop()
    result = 0
    stack = []
    k = len(new)
    for i in range(k):
        if '0' <= new[i] <= '9':
            stack.append(new[i])
        else:
            right = int(stack.pop())
            left = int(stack.pop())

            if new[i] == '+':
                result = right + left
            else:
                result = right * left
            stack.append(result)
    print(f"#{tc} {result}")