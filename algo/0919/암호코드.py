# import sys
# sys.stdin = open("input.txt", "r")

def find_code(x):
    num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    result = [0]
    true_num = 0
    one = 0
    two = 0
    for i in range(0,56,7):
        a = x[i:i+7]
        for j in range(10):
            if num[j] == a:
                result.append(j)
                true_num += j
    for i in range(9):
        if i%2 == 1:
            one += result[i] * 3
        else:
            two += result[i]
    if (one + two)%10 == 0:
        return true_num
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    code = ''
    for i in range(N):
        problem = input()
        if '1' not in problem:
            continue
        else:
            for i in range(M-1,-1,-1):
                if problem[i] == '1':
                    a = i
                    break
            for j in range(a, a-56, -1):
                code = problem[j] + code

    print(f"#{tc} {find_code(code)}")


