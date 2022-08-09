T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    max_num = 0
    min_num = 3000000000
    for i in range(N-M+1):
        x = 0
        for j in range(i, i+M):
            x += a[j]
        if x >= max_num:
            max_num = x
        if x <= min_num:
            min_num = x
    print(f"#{tc} {max_num - min_num}")