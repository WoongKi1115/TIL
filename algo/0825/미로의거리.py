T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = [0] * (N * N)
    front = rear = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                a, b = i, j
            if maze[i][j] == 3:
                gi, gj = i, j
    q[rear] = (a, b)
    rear += 1
    count = 0
    while True:
        size = rear - front
        count += 1
        for _ in range(size):
            x = q[front]
            front += 1
            for d in range(4):
                Ni = di[d] + x[0]
                Nj = dj[d] + x[1]
                if 0 <= Ni < N and 0 <= Nj < N and visited[Ni][Nj] == 0 and maze[Ni][Nj] != 1:
                    q[rear] = (Ni, Nj)
                    rear += 1
                    visited[Ni][Nj] = 1

        if visited[gi][gj] == 1:
            count -= 1
            break
        if front == rear:
            count = 0
            break

    print(f"#{tc} {count}")
