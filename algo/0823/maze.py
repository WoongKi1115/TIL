T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                a, b = i, j
                break
    s = (a, b)
    stack = []
    i = a
    j = b
    while True:
        visited[i][j] = 1
        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((i, j))
                i = ni
                j = nj
                break
        else:
            if len(stack)== 0:
                print(f"#{tc} 0")
                break

            else:
                i,j = stack.pop()
        if maze[i][j] == 3:
            print(f"#{tc} 1")
            break