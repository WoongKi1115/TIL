T = int(input())
for tc in range(1, T+1):
    stack = []
    word = list(input().split())
    for i in word:
        stack.append(i)
    result = ''
    for i in range(len(stack)):
        result += stack.pop()
        result += ' '
    print(f"Case #{tc}: {result}")