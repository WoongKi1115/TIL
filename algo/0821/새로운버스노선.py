T = int(input())
for tc in range(1,T+1):
    N = int(input())
    box = [list(map(int,input().split())) for _ in range(N)]
    count = [0]*1001
    for i in range(N):
        if box[i][0] == 1:
            for j in range(box[i][1], box[i][2]+1):
                count[j] += 1
        if box[i][0] == 2:
            for j in range(box[i][1], box[i][2]+1,2):
                count[j] += 1
        if box[i][0] == 3:
            if box[i][1]%2 == 0:
                for j in range(box[i][1], box[i][2] + 1):
                    if j%4 == 0:
                        count[j] += 1
            else:
                for j in range(box[i][1], box[i][2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        count[j] += 1
    max_count = 0
    for i in range(1001):
        if count[i] > max_count:
            max_count = count[i]
    print(f"#{tc} {max_count}")


