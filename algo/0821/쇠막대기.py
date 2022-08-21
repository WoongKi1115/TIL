T = int(input())
for tc in range(1,T+1):
    problem = list(input())
    stack = []
    for i in range(len(problem)):
        if problem[i] == '(':
            stack.append(problem[i])