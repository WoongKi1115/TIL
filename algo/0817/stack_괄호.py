# 괄호 문자열 입력
bracket = input()

stack = []

answer = 1 # 1은 괄호가 잘 되어있다, 0은 괄호가 잘 안되어있다.

for c in bracket: # 괄호 문자열에서 괄호 하나씩 떼오기
    if c == "(":
        # 괄호가 열리면 왼쪽괄호 추가
        stack.append(c)
    elif c == ")":
        if len(stack) == 0:
            # 괄호가 열린적이 없는데 닫으려고 한다 ==> 잘못됬다.
            answer = 0 # 잘못됬다고 체크
            break
        stack.pop(-1) # 열린 괄호 , 닫힌 괄호 쌍 완성

if len(stack) > 0 : # 스택에 남은 괄호가 있다. ==> 제대로 괄호가 닫히지 않았다.
    answer = 0

print(answer)
#()()((()))                         1
#((()((((()()((()())((())))))       0
#())                                0
#(((                                0
#))                                 0
