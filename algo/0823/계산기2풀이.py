T = 10
for tc in range(1,T+1):
    n = int(input())
    exp = input()
    postfix = ''
    icp = {'+' : 1, '*' : 2}
    stack = []
    for i in range(n):
        # 글자 하나씩 떼서 보는데
        # 연산자 or 피연산자
        if '0' <= exp[i] <='9':
            # 피연산자면 그냥 결과 문자열에 이어 붙이기
            postfix += exp[i]
        else:
            # 연산자면 스택의 꼭대기를 확인
            # 자신보다 같거나 높은 우선순위를 가진 연산자가 있으면 꺼냄.
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()
            stack.append(exp[i])
    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    result = 0
    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 그냥 넘어감
        # 스택에다가 담는다
        if '0' <= postfix[i] <= '9':
            stack.append(postfix[i])
            # 연산자가 나오면 계산
            # 스택에서 두개의 피연산자 꺼냄
        else:
            # 연산자가 나오면 계산 (앞의 두 피연산자를 선택)
            # 스택에서 두개의 피 연산자 꺼냄
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == '+':
                result = right + left
            else:
                result = right * left
            stack.append(result)
    print(f"#{tc} {result}")
