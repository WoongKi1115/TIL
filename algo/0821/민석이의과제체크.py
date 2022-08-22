T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    list1 = list(map(int,input().split()))
    count = [0]*(N+1)
    print(f"#{tc}", end = ' ')
    for i in list1:
        count[i] += 1
    for i in range(1,N+1):
        if count[i] != 1:
            print(i, end = ' ')
    print()