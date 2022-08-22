T = int(input())
for tc in range(1,T+1):
    problem = list(input())
    stack = []
    count = [0]*(len(problem)+1)
    a = 0
    result = 0
    for i in range(len(problem)):
        if problem[i] == '(' and problem[i+1] != ')':
            a += 1
        elif problem[i] == ')':
            if problem[i-1] == '(':
                result += (a)
            else:
                result += 1
                a -= 1


    print(f"#{tc} {result}")
