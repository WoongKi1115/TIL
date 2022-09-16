def bfs(i, j):
    global result
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = [[0]*N for _ in range(N)]
    if box[i][j] == 1:
        house = 1
    else:
        house = 0
    queue = []
    queue.append((i,j))
    visited[i][j] = 1
    K = 1
    cost = K*K + (K-1)*(K-1)
    house_pay = house * M
    if house_pay - cost >= 0 and result < house:
        result = house
    while queue:
        size = len(queue)
        K += 1
        for _ in range(size):
            i, j = queue.pop(0)
            for d in range(4):
                ci = i + di[d]
                cj = j + dj[d]
                if 0<= ci <N and 0 <= cj < N and visited[ci][cj] == 0:
                    if box[ci][cj] == 1:
                        house += 1
                    visited[ci][cj] = 1
                    queue.append((ci, cj))
        cost = K * K + (K - 1) * (K - 1)
        house_pay = house * M
        if house_pay - cost >= 0 and result < house:
            result = house




T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    print(f"#{tc} {result}")