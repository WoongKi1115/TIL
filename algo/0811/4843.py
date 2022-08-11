T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    count = [0]*N
    s = 0
    e = -1
    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    for i in range(N):
        if i%2 != 0:
            count[i] = num[s]
            s += 1
        else:
            count[i] = num[e]
            e -= 1
    print(f"#{tc}",end = ' ')
    for i in range(N):
        print(count[i], end = ' ')
    print()

