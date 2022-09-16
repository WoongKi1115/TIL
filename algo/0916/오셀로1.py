di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, 1, -1, 1, -1]


def find(a, b, c):
    for d in range(8):
        ci = b + di[d]
        cj = a + dj[d]
        if 0 <= ci < N and 0 <= cj < N and box[ci][cj] != 0 and box[ci][cj] != c:
            flag = False
            stack = []
            while True:
                stack.append([ci, cj])
                ci += di[d]
                cj += dj[d]
                if ci < 0 or ci > (N - 1) or cj < 0 or cj > (N - 1):
                    break
                elif box[ci][cj] == 0:
                    break
                elif box[ci][cj] == c:
                    flag = True
                    break
            if flag:
                for s in stack:
                    box[s[0]][s[1]] = c


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    box = [[0] * N for _ in range(N)]
    box[N // 2 - 1][N // 2 - 1] = 2
    box[N // 2][N // 2] = 2
    box[N // 2 - 1][N // 2] = 1
    box[N // 2][N // 2 - 1] = 1
    for _ in range(M):
        x, y, color = map(int, input().split())
        x = x - 1
        y = y - 1
        find(x, y, color)
        box[y][x] = color

    count_1 = 0
    count_2 = 0
    for i in range(N):
        for j in range(N):
            if box[i][j] == 1:
                count_1 += 1
            elif box[i][j] == 2:
                count_2 += 1
    print(f"#{tc} {count_1} {count_2}")
