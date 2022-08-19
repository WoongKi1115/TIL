T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    list1 = [list(map(int,input().split())) for _ in range(Q)]
    count = [0] * 1001
    for i in range(Q):
        for j in range(list1[i][0], list1[i][1]+1):
            count[j] = i+1

    print(f"#{tc} {' '.join(map(str,count[1:N+1]))}")
