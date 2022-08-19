T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = 0
            for x in range(M):
                for y in range(M):
                    if 0 <= i + x < N and 0 <= j + y < N:
                        count += box[i + x][j + y]
            if count > max_count:
                max_count = count
    print(f"#{tc} {max_count}")
