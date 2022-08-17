T = int(input())
for tc in range(1, T+1):
    case = int(input())
    num = list(map(int,input().split()))
    max_num = num[-1]
    count = 0
    margin = 0
    sum_num = 0
    for i in range(len(num)-2,-1,-1):
        if num[i] > max_num:
            margin += (count * max_num) - sum_num
            max_num = num[i]
            count = 0
            sum_num = 0
        elif num[i] <= max_num:
            count += 1
            sum_num += num[i]
            if i == 0:
                margin += (count * max_num) - sum_num
    print(f"#{tc} {margin}")