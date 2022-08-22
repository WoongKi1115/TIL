T = 10
for tc in range(1, T + 1):
    N = int(input())
    problem = input()
    stack1 = [0]*N
    top = -1

    a = {'+': 1, '*': 2}
    after = ''
    for i in range(N):
        if '1' <= problem[i] <= '9':
            after += problem[i]
        else:
            if top > -1 and a[stack1[top]] >= a[problem[i]]:
                after += stack1[top]
                top -= 1
            top += 1
            stack1[top] = problem[i]
    while top > -1:
        after += stack1[top]
        top -= 1
    stack2 = []
    for i in range(len(after)):
        if '1' <= after[i] <= '9':
            stack2.append(after[i])
        else:
            x = stack2.pop()
            y = stack2.pop()
            if after[i] == '+':
                stack2.append(int(x)+int(y))
            elif after[i] == '*':
                stack2.append(int(x)*int(y))
    print(f"#{tc} {stack2[-1]}")
