di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = 10
for tc in range(1, T + 1):
    answer = 0
    n = int(input())
    map = [list(input()) for _ in range(16)]

    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if map[i][j] == '2':
                x, y = i, j

    stack = [(x, y)]
    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < 16 and 0 <= nj < 16:
                if map[ni][nj] == '0':
                    stack.append((ni, nj))
                    map[ni][nj] = '9'
                elif map[ni][nj] == '3':
                    answer = 1
                    stack.clear()
                    break

    print(f'#{tc} {answer}')