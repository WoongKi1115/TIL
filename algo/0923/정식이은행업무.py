def check2(a):
    num_a = 0
    x = -1
    for i in range(len(a) - 1, -1, -1):
        x += 1
        if int(a[i]) == 0:
            continue
        else:
            num_a += int(a[i]) * 2 ** x
    return num_a

def check3(a):
    num_a = 0
    x = -1
    for i in range(len(a) - 1, -1, -1):
        x += 1
        if int(a[i]) == 0:
            continue
        else:
            num_a += int(a[i]) * 3 ** x
    return num_a


T = int(input())
for tc in range(1, T + 1):
    two = list(input())
    three = list(input())
    flag = False
    result = 0
    for i in range(len(two)):
        x = two[i]
        if two[i] == '0':
            two[i] = '1'
        else:
            two[i] = '0'
        for j in range(len(three)):
            y = three[j]
            for k in range(3):
                three[j] = str(k)
                if check2(two) == check3(three):
                    flag = True
                    result = check2(two)
                    break
            if flag == True:
                break

            three[j] = y
        two[i] = x



    print(f"#{tc} {result}")

