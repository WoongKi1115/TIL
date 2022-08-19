T = 10
for tc in range(1, 11):
    num, pw = input().split()
    stack = []
    for i in range(int(num)):
        if len(stack) == 0 or stack[-1] != pw[i]:
            stack.append(pw[i])
        else:
            stack.pop()
    result = ''
    for i in stack:
        result += i
    print(f"#{tc} {result}")
