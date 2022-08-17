T = int(input())
for tc in range(1, T+1):
    list1 = []
    str1 = input()
    str2 = input()
    list1 += str1[0]
    for i in range(0,len(str1)):
        if str1[0] != str1[i]:
            list1 += [str1[i]]
        else:
            continue
    print(list1)
    max_count = 0
    for j in list1:
        count = 0
        for k in range(len(str2)):
            if str2[k] == j:
                count += 1
        if count >= max_count:
            max_count = count
    print(f"#{tc} {max_count}")