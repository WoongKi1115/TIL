T = 10
N = 100 # 10 X 10
for i in range(T):
    tc = int(input())
    box = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        sum_x = 0
        sum_xy = 0
        sum_yx = 0
        for j in range(N):
            sum_x += box[i][j]
        if sum_x > result:
            result = sum_x
        if i == j:
            sum_xy += box[i][j]
            if sum_xy > result:
                result = sum_xy
        elif i + j == N-1:
            sum_yx += box[i][j]
            if sum_yx > result:
                result = sum_yx
    for j in range(N):
        sum_y = 0
        for i in range(N):
            sum_y += box[i][j]
        if sum_y > result:
            result = sum_y
    print(f"#{tc} {result}")
