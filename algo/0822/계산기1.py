T = 10
for tc in range(1,T+1):
    N = int(input())
    problem = input()
    stack = [0]*N
    top = -1
    new = ''
    for i in range(N):
        if '0' <= problem[i] <= '9':
            new += problem[i]
        else:
            top += 1
            stack[top] = problem[i]
    while top > -1:
        new += stack[top]
        top -= 1
    stack2 = []
    for i in range(N):
        if '0'<= new[i] <= '9':
            stack2.append(new[i])

        else:
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(int(num1)+int(num2))
    print(f"#{tc} {stack2[-1]}")