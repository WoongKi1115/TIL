T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        count1 = 0
        for j in range(N):
            if box[i][j] == 1:
                count1 += 1
            elif box[i][j] == 0:
                if count1 == K:
                    result += 1
                count1 = 0
        if count1 == K:
            result += 1

    for j in range(N):
        count2 = 0
        for i in range(N):
            if box[i][j] == 1:
                count2 += 1
            elif box[i][j] == 0:
                if count2 == K:
                    result += 1
                count2 = 0
        if count2 == K:
            result += 1

    print(f"#{tc} {result}")
