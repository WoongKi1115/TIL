T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(N)]
    di1 = [-1, 1, 0, 0]   # i 상하좌우
    dj1 = [0, 0, -1, 1]   # j 상하좌우
    di2 = [-1, 1, 1, -1]  # i 시계방향
    dj2 = [1, 1, -1, -1]  # j 시계방향
    d = 0
    max_num = 0
    for i in range(N):      # + 방향 계산
        for j in range(N):
            count = box[i][j]
            for m in range(M):
                for x in range(4):
                    if m == 0:
                        continue
                    elif 0 <= i+(di1[x]*m) <= N-1 and 0 <= j+(dj1[x]*m) <= N-1:
                        count += box[i+(di1[x]*m)][j+(dj1[x]*m)]
            if count > max_num:
                max_num = count

    for i in range(N):      # x 방향 계산
        for j in range(N):
            count = box[i][j]
            for m in range(M):
                for x in range(4):
                    if m == 0:
                        continue
                    elif 0 <= i+(di2[x]*m) <= N-1 and 0 <= j+(dj2[x]*m) <= N-1:
                        count += box[i+(di2[x]*m)][j+(dj2[x]*m)]
            if count > max_num:
                max_num = count
    print(f"#{tc} {max_num}")


