T = int(input())
for tc in range(1, T+1):
    testcase, num = input().split()
    list1 = list(map(str, input().split()))
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    j = 0
    k = 0
    for i in range(int(num)):
        if list1[i] == 'ZRO':
            a += 1
        elif list1[i] == 'ONE':
            b += 1
        elif list1[i] == 'TWO':
            c += 1
        elif list1[i] == 'THR':
            d += 1
        elif list1[i] == 'FOR':
            e += 1
        elif list1[i] == 'FIV':
            f += 1
        elif list1[i] == 'SIX':
            g += 1
        elif list1[i] == 'SVN':
            h += 1
        elif list1[i] == 'EGT':
            j += 1
        elif list1[i] == 'NIN':
            k += 1
    result = 'ZRO '*a + 'ONE '*b + 'TWO '*c + 'THR '*d + 'FOR '*e + 'FIV '*f + 'SIX '*g + 'SVN '*h + 'EGT '*j + 'NIN '*k
    print(f"{testcase}\n{result}")