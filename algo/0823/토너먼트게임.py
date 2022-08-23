T = int(input())


def rsp(a, b):
    if a[1] == '1' and b[1] == '2':
        return b
    elif a[1] == '1' and b[1] == '3':
        return a
    elif a[1] == '2' and b[1] == '1':
        return a
    elif a[1] == '2' and b[1] == '3':
        return b
    elif a[1] == '3' and b[1] == '1':
        return b
    elif a[1] == '3' and b[1] == '2':
        return a


for tc in range(1, T + 1):
    N = int(input())
    list1 = list(input().split())
    print(list1)
    stack1 = []
    stack2 = []
    for i in range(1, N + 1):
        stack1.append((i, list1[i - 1]))

    while True:
        if len(stack1) + len(stack2) != 1:
            break
        else:
            for _ in range(len(stack1) // 2 + 1):
                if len(stack1) >= 2:
                    num1 = stack1.pop()
                    num2 = stack1.pop()
                    if num1[1] == num2[1]:
                        if num1[0] > num2[0]:
                            stack2.append(num2)
                        else:
                            stack2.append(num1)
                    else:
                        stack2.append(rsp(num1, num2))

                else:
                    stack2.append(stack1[-1])
                    break

            for _ in range(len(stack2) // 2 + 1):
                if len(stack2) >= 2:
                    num1 = stack2.pop()
                    num2 = stack2.pop()
                    if num1[1] == num2[1]:
                        if num1[0] > num2[0]:
                            stack1.append(num2)
                        else:
                            stack1.append(num1)
                    else:
                        stack1.append(rsp(num1, num2))

                else:
                    stack1.append(stack2[-1])
                    break
    if len(stack1) == 1:
        print(stack1[-1][0])
    elif len(stack2) == 1:
        print(stack2[-1][0])
