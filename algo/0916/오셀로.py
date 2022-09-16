def hor(a, b, c):
    di = [-1, 1, 1, -1]
    dj = [1, -1, 1, -1]
    global box
    for i in range(N):
        if box[b][i] == c:
            if i < a:
                for j in range(i + 1, a):
                    box[b][i] = c
            else:
                for j in range(a, i):
                    box[b][i] = c
            break
    for i in range(N):
        if box[i][a] == c:
            if i < a:
                for j in range(i + 1, a):
                    box[i][a] = c
            else:
                for j in range(a, i):
                    box[i][a] = c
            break
    ci = 0
    cj = 0

    d = 0
    while 0 <= ci < N and 0 <= cj < N:
        for d in range(4):
            ci = b + di[d]
            cj = a + dj[d]
            if box[ci][cj] == c:
                pass
        a = cj
        b = ci


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    box = [[0] * N for _ in range(N)]
    for _ in range(M):
        x, y, color = map(int, input().split())
        x = x - 1
        y = y - 1

        box[y][x] = color
