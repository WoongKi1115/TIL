T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list1= list(map(int,input()))
    count = 0
    max_count = 0
    for i in range(1,N):
        if list1[i-1] == 1 and list1[i] == 1:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
    print(f"#{tc} {max_count}")