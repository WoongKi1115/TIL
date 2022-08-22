# 중위연산식 ==> 후위연산식
# 2+3*4/5
n = int(input())  # 식의 길이(문자 갯수)
infix = input()  # 중위표기식을 문자열로 입력 받기

stack = [0] * n  # 스택의 길이는 최대 n
top = -1

# 연산자의 우선순위
icp = {"+": 1, "-": 1, "/": 2, "*": 2}

postfix = ""

# 중위연산식을 순회하면서 후위연산식으로 바꾸기
for i in range(n):
    # i 번째 문자를 하나 떼와서
    # 피연산자이면 ==> 출력, 연산자이면 우선순위 스택의 top과 비교
    if "0" <= infix[i] <= "9": # 피연산자, 숫자인경우
        postfix += infix[i] # 문자열 조합
    else:
        # 연산자인 경우
        # 우선순위를 비교해서 스택의 top 의 원소와 지금 떼온 연산자와 우선순위를 비교
        # 우선순위가 같거나 높으면 pop
        if top > -1 and icp[stack[top]] >= icp[infix[i]]:
            # pop 시켜주고 문자열에 출력
            postfix += stack[top]
            top -= 1
        top += 1
        stack[top] = infix[i]

# 만약 스택 안에 연산자가 남아있는 경우 수식 뒤에 붙여주기
while top > -1:
    postfix += stack[top]
    top -= 1

print(postfix) # 후위연산식 출력
