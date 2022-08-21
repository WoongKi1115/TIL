T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list1 = list(map(int,input().split()))
    for i in range(N-1,0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    print(f"#{tc}", end = ' ')
    for i in list1:
        print(i, end = ' ')
    print()