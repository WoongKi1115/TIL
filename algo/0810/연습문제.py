T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x = [list(map(int,input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:    #인덱스 검사 과정
                    if x[ni][nj]-x[i][j] >= 0:
                        sum += (x[ni][nj]-x[i][j])
                    else:
                        sum += -1 * (x[ni][nj]-x[i][j])
    print(f"#{tc} {sum}")
