T = int(input())
for tc in range(1,T+1):
    problem = list(input().split())
    stack = []
    count1 = 0
    count2 = 0
    result = ''
    for i in range(len(problem)-1):
        if '0' <= problem[i] <= '9':
            count1 += 1
        else:
            count2 += 1
    if count1 != count2+1:
        result = 'error'
        print(f"#{tc} {result}")
        continue

    for i in range(len(problem)-1):
        if '0' <= problem[i] <= '9':
            stack.append(problem[i])
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if problem[i] == '+':
                stack.append(num1 + num2)
            elif problem[i] == '-':
                stack.append(num2-num1)
            elif problem[i] == '/':
                stack.append(num2//num1)
            else:
                stack.append(num1*num2)
    if len(stack) != 0:
        print(f"#{tc} {stack[-1]}")
