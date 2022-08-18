T = int(input())
for tc in range(1,T+1):
    word = input()
    stack =[]
    for i in range(len(word)):
        if len(stack) == 0 or stack[-1] != word[i]:
            stack.append(word[i])
        else:
            stack.pop()
    print(f"#{tc} {len(stack)}")