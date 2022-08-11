T = int(input())

for tc in range(1,T+1):
    N = int(input())
    box = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        aj, ai, bj, bi, color = map(int,input().split())
        count = 0
        for i in range(ai, bi+1):
            for j in range(aj, bj+1):
                if box[i][j] != 0:
                    box[i][j] = 3
                else:
                    box[i][j] = color

    for x in range(10):
        for y in range(10):
            if box[y][x] == 3:
                count += 1

    print(f"#{tc} {count}")


