T = int(input())
for tc in range(1,T+1):
    list1 = list(map(int,input().split()))
    max_num = 0
    for i in range(len(list1)):
        if list1[i] > max_num:
            max_num = list1[i]
    print(f"#{tc} {max_num}")
