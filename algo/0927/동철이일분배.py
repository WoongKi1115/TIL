def work(cnt, x):
    global max_num
    if cnt == N:
        if x > max_num:
            max_num = x
        return
    if x <= max_num:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            work(cnt+1, x*box[cnt][i]/100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_num = 0
    work(0, 1)
    max_num *= 100
    print(f"#{tc} {round(max_num,6):.6f}")