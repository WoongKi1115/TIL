T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list1 = []
    for i in range(1,N+1):
        a, b = map(int,input().split())
        if b < a:
            a, b = b, a
        if a % 2 == 0:
            a -= 1
        if b % 2 == 1:
            b += 1
        list1.append([a,b])
    count = [0]*402
    for i in range(N):
        for j in range(list1[i][0], list1[i][1]+1):
            count[j] += 1
    max_count = 0
    for i in range(401):
        if count[i] > max_count:
            max_count = count[i]
    print(f"#{tc} {max_count}")

