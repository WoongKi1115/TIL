T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N):
        count1 = 1
        for j in range(1,M):
            if box[i][j] == 1 and box[i][j-1] == 1:
                count1 += 1
            else:
                count1 = 1
            if count1 > max_count:
                max_count = count1
    for j in range(M):
        count2 = 1
        for i in range(1, N):
            if box[i][j] == 1 and box[i-1][j] == 1:
                count2 += 1
            else:
                count2 = 1
            if count2 > max_count:
                max_count = count2
    print(f"#{tc} {max_count}")

