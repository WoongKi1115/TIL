T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list1 = list(map(int,input().split()))
    max_count = 0
    count = 1
    for j in range(1,N):
        if list1[j] > list1[j-1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
    print(f"#{tc} {max_count}")
